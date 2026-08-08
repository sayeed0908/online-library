import os

from django.http import JsonResponse
from django.views.decorators.http import require_POST

from google import genai

from books.models import Book


@require_POST
def ai_chat(request):

    message = request.POST.get("message", "").strip()

    if not message:
        return JsonResponse({
            "success": False,
            "error": "Please enter a message."
        }, status=400)

    api_key = os.environ.get("GEMINI_API_KEY")

    if not api_key:
        return JsonResponse({
            "success": False,
            "error": "Gemini API key is not configured."
        }, status=500)

    try:

        # Get books from the database
        books = Book.objects.all().order_by("-created_at")

        if books.exists():

            library_data = []

            for book in books:

                library_data.append(
                    f"""
Book Name: {book.book_name}
Author: {book.author}
Publisher: {book.publisher}
Source: {book.source}
Pages: {book.total_pages}
Price: {book.price}
Category: {book.category}
Description: {book.description}
"""
                )

            library_context = "\n".join(library_data)

        else:

            library_context = "There are currently no books in the library database."


        # AI instructions
        prompt = f"""
You are the official AI assistant for an Online Library.

Answer the user's question clearly, politely and helpfully.

IMPORTANT RULES:

1. Use the library database information below when the user asks about
   books, authors, prices, categories, publishers, pages or availability.

2. Never invent a book, price, author or other library information.

3. If the requested information is not available in the database,
   clearly say that the information is not currently available.

4. You can answer general questions too.

5. Keep answers concise and easy to understand.

6. If the user asks how to order a book, explain that they can open
   the book details page and use the available ordering option.

LIBRARY DATABASE:

{library_context}

USER QUESTION:

{message}
"""


        client = genai.Client(api_key=api_key)


        response = client.models.generate_content(
            model="gemini-3.6-flash",
            contents=prompt,
        )


        return JsonResponse({
            "success": True,
            "reply": response.text
        })


    except Exception:

        return JsonResponse({
            "success": False,
            "error": "AI service is temporarily unavailable."
        }, status=500)
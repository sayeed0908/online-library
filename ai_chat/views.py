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

            library_context = (
                "There are currently no books in the library database."
            )

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

        print("GEMINI: Starting request...", flush=True)

        client = genai.Client(api_key=api_key)

        print("GEMINI: Client created...", flush=True)

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt,
        )

        print("GEMINI: Response received...", flush=True)

        reply = response.text

        if not reply:
            return JsonResponse({
                "success": False,
                "error": "Gemini returned an empty response."
            }, status=500)

        return JsonResponse({
            "success": True,
            "reply": reply
        })

    except Exception as e:

        error_message = repr(e)

        print("GEMINI AI ERROR:", error_message, flush=True)

        return JsonResponse({
            "success": False,
            "error": error_message
        }, status=500)
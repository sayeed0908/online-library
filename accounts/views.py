from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import RegisterForm


def register(request):

    if request.method == "POST":

        form = RegisterForm(request.POST)

        if form.is_valid():

            form.save()

            return redirect("login")

    else:

        form = RegisterForm()

    return render(request, "accounts/register.html", {
        "form": form
    })


def user_login(request):

    if request.method == "POST":

        email = request.POST.get("email")
        password = request.POST.get("password")

        user = authenticate(
            request,
            username=email,
            password=password
        )

        if user is not None:

            login(request, user)

            return redirect("book_list")

        else:

            return render(request, "accounts/login.html", {
                "error": "Invalid email or password."
            })

    return render(request, "accounts/login.html")


# Logout
def user_logout(request):

    logout(request)

    return redirect("home")
from django.shortcuts import render, redirect
from django.contrib import messages
from ..forms import RegisterForm
from django.contrib.auth import authenticate, login

def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user=form
            form.save()
            messages.info(request, "Thanks for registering. You are now logged in.")
            user = authenticate(username=form.cleaned_data['username'],
                                    password=form.cleaned_data['password1'],)
            login(request, user)
            return redirect('/')
    else:
        form = RegisterForm()
    return render(request, "register/register.html", {"form": form})

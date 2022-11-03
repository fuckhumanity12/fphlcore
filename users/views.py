from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import *
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin


class Login(LoginView):
    template_name = "users/login.html"
    # def get(self, request, *args, **kwargs):
    #     return render(request, "users/login.html")

    # def post(self, request, *args, **kwargs):
    #     form = LoginForm(request.POST)
    #     if form.is_valid():
    #         try:
    #             useracc = authenticate(username=form.cleaned_data.get(
    #                 "username"), password=form.cleaned_data.get("password"),)
    #             login(request, useracc)
    #             messages.success(request, 'Successful')
    #         except:
    #             messages.warning(request, 'Data Is Incorrect')
    #             return render(request, 'users/login.html')
    #     else:
    #         messages.warning(request, "Form Incorrect")
    #     return render(request, "users/login.html")


class Register(View):
    def get(self, request, *args, **kwargs):
        return render(request, "users/register.html")

    def post(self, request, *args, **kwargs):
        form = SignupForm(request.POST)
        if form.is_valid():

            user_email = User.objects.filter(
                email=form.cleaned_data.get('email'))
            user_name = User.objects.filter(
                username=form.cleaned_data.get('username').lower())

            if user_email.exists():
                messages.warning(
                    request, f"A User With The Email: {form.cleaned_data.get('email')} Already Exists")
            elif user_name.exists():
                messages.warning(
                    request, f"A User With The Username: {form.cleaned_data.get('username')} Already Exists")
            else:
                form.username = request.POST.get("username").lower()
                user = form.save()
                users = authenticate(username=user.username,
                                     password=form.cleaned_data.get("password1"))
                login(request, users)
                messages.success(request, "Successfully Logged In!")
                return redirect("register")
            return render(request, "users/register.html")
        else:
            messages.warning(request, "form invalid")
            return render(request, "users/register.html")

from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import *
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash


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
        if request.user.is_authenticated:
            messages.success(request, "You Are Already Registered 😺")
            return redirect("home")
        return render(request, "users/register.html")

    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            messages.success(request, "You Are Already Registered 😺")
            return redirect("home")
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


class Logout(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        messages.warning(request, "Logged Out Successfully")
        return redirect("home")


class ChangePassword(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        form = PasswordChangeForm(request.user)
        return render(request, "users/change-password.html", {"form": form, })

    def post(self, request, *args, **kwargs):
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, "Successfully Changed!")
            return redirect("home")
        else:
            messages.warning(request, "Error In Data Provided")
        return render(request, "users/change-password.html")


class DelAccountConf(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        return render(request, "users/delete-account-conf.html")


class DelAccount(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        user = User.objects.get(username=request.user)
        user.delete()
        messages.info(request, "Account Successfully Deleted 😭")
        return redirect("home")


# class UpdateEmail(LoginRequiredMixin, View):
#     def get(self, request, *args, **kwargs):
#         return render(request, "users/update-email.html")

#     def post(self, request, *args, **kwargs):
#         form = UpdateEmail(request.POST)
#         if form.is_valid():
#         user = User.objects.get(username=request.user.username)
#         user.email = form.cleaned_data.get("email")
#         user.save()
#         else:
#             messages.warning(request, "Invalid")
#             return render(request, "users/update-email.html")
#         return redirect("home")

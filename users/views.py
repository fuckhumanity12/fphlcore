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


class Login(View):
    # template_name = "users/login.html"
    def get(self, request, *args, **kwargs):
        return render(request, "users/login.html")

    def post(self, request, *args, **kwargs):
        username = request.POST.get("username").lower().replace(" ", "")
        password = request.POST.get("password")
        try:
            users = authenticate(username=username, password=password)
            login(request, users)
            messages.success(request, "Successfully Logged In!")
            return redirect("home")
        except:
            messages.warning(request, "Your Data Is Incorrect")
        return render(request, "users/login.html")


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
        username = request.POST.get("username").lower().replace(" ", "")
        email = request.POST.get("email").lower().replace(" ", "")
        password = request.POST.get("password1")
        password2 = request.POST.get("password2")
        theredot = False
        thereat = False
        for i in email:
            if i == ".":
                theredot = True
            if i == "@":
                thereat = True
        if password == password2:
            if not User.objects.filter(username=username).exists():
                if email != "" or email != " " or email == None:
                    if thereat and theredot:
                        user = User.objects.create_user(
                            email=email, username=username, password=password)
                        users = authenticate(username=user.username,
                                             password=password)
                        login(request, users)
                        messages.success(
                            request, "Successfully Created Account!")
                        return redirect("home")
                    else:
                        messages.warning(request, "Email Invalid!")
                else:
                    messages.warning(request, "Email Cannot Be Empty")
            else:
                messages.warning(
                    request, "Username Is Already Taken, Choose Another One")

        else:
            messages.warning(request, "Passwords do not match")
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
        user.is_active = False
        user.save()
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

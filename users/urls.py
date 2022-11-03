from django.urls import path
from .views import *
urlpatterns = [
    path("login/", Login.as_view(), name="login"),
    path("register/", Register.as_view(), name="register"),
    path("", home.as_view(), name="home"),
]

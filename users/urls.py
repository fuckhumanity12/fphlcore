from django.urls import path
from .views import *
urlpatterns = [
    path("login/", Login.as_view(), name="login"),
    path("register/", Register.as_view(), name="register"),
    path("logout/", Logout.as_view(), name="logout"),
    path("change-password/", ChangePassword.as_view(), name="change-password"),
    path("del-acc-conf/", DelAccountConf.as_view(), name="accdel-conf"),
    path("acc-del/", DelAccount.as_view(), name="acc-del"),
    # path("update-email/", UpdateEmail.as_view(), name="update-email"),
]

from django.urls import path
from .views import *
urlpatterns = [
    path("", ArticlesList.as_view(), name="home"),
    path("article/<str:pk>", ArticleDetail.as_view(), name="article-detail"),
]

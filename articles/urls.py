from django.urls import path
from .views import *
urlpatterns = [
    path("", ArticlesList.as_view(), name="home"),
    path("article/<str:pk>/", ArticleDetail.as_view(), name="article-detail"),
    path("save/<str:pk>/", SaveArticles.as_view(), name="save-article"),
    path("remove-save/<str:pk>/", RemoveSave.as_view(), name="remove-save"),
    path("account/", AccountPage.as_view(), name="account"),
    # path("comment/<str:article>", CommentView.as_view(), name="comment"),
]

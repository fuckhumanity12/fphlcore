from django.shortcuts import render, redirect
from django.views import View
from .models import *
from django.contrib import messages


class ArticlesList(View):
    def get(self, request, *args, **kwargs):
        Articles = Article.objects.all().order_by("-date")
        return render(request, "articles/home.html", {"articles": Articles, })


class ArticleDetail(View):
    def get(self, request, pk, *args, **kwargs):
        if Article.objects.filter(id=pk).exists():
            article = Article.objects.get(id=pk)
            context = {"article": article, }
        else:
            messages.warning(request, "This Article Doesn't Exists")
            return redirect("home")
        return render(request, "articles/article-detail.html", context)

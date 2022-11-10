from django.shortcuts import render, redirect
from django.views import View
from articles.models import Article
from django.contrib import messages
from .models import *
from django.contrib.auth.mixins import LoginRequiredMixin


class ListChanges(View):
    def get(self, request, pk, *args, **kwargs):
        if Article.objects.filter(id=pk).exists():
            article = Article.objects.get(id=pk)
            changes = ArticleHistory.objects.filter(article=article)
        else:
            messages.warning(request, "Article Does not Exist")
            return redirect("home")
        return render(request, "wiki/list-changes.html", {"changes": changes, "article": article, })


class EditArticle(LoginRequiredMixin, View):
    def get(self, request, pk, *args, **kwargs):
        if Article.objects.filter(id=pk).exists():
            article = Article.objects.get(id=pk)
        else:
            messages.warning(request, "Article Does not Exist")
            return redirect("home")
        return render(request, "wiki/edit-article.html", {"article": article, })

    def post(self, request, pk, *args, **kwargs):
        if Article.objects.filter(id=pk).exists():
            article = Article.objects.get(id=pk)
            if request.POST.get("newarti") == article.content:
                messages.warning("No Changes Were Made")
                return redirect("article-detail", article.id)
            else:
                saved = ArticleHistory.objects.create(
                    maker=request.user, article=article, oldtext=article.content, newtext=request.POST.get("newarti"), changetext=request.POST.get("editreason"))
                messages.success(
                    request, "Changes Were Successfully Submitted, And Will Be Reviewed Before Publication Or Declining")
                return redirect("article-detail", article.id)
        else:
            messages.warning(request, "Article Does not Exist")
            return redirect("home")

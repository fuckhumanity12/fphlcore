from django.shortcuts import render, redirect
from django.views import View
from .models import *
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import *
from django.db.models import Q


class ArticlesList(View):
    def get(self, request, *args, **kwargs):
        Articles = Article.objects.all().order_by("-date")
        return render(request, "articles/home.html", {"articles": Articles, })


class ArticleDetail(View):
    def get(self, request, pk, *args, **kwargs):
        if Article.objects.filter(id=pk).exists():
            article = Article.objects.get(id=pk)
            # comments = Comment.objects.filter(article=article)
            context = {"article": article, }  # "comments": comments,
        else:
            messages.warning(request, "This Article Doesn't Exists")
            return redirect("home")
        return render(request, "articles/article-detail.html", context)


class SaveArticles(LoginRequiredMixin, View):
    def get(self, request, pk, *args, **kwargs):
        if Article.objects.filter(id=pk).exists():
            article = Article.objects.get(id=pk)
            if Saved.objects.filter(articles=article, owner=request.user).exists():
                messages.success(request, "This Article Is Already Saved")
            else:
                newsave = Saved.objects.get(owner=request.user)
                newsave.articles.add(article)
                messages.success(request, "Successfully Added Article!")
        else:
            messages.warning(request, "This Article Doesn't Exists")
        return redirect("home")


class RemoveSave(LoginRequiredMixin, View):
    def get(self, request, pk, *args, **kwargs):
        if Article.objects.filter(id=pk).exists():
            article = Article.objects.get(id=pk)
            if Saved.objects.filter(articles=article, owner=request.user).exists():
                newsave = Saved.objects.get(owner=request.user)
                newsave.articles.remove(article)
                messages.warning(request, "Successfully Removed Article!")
            else:
                messages.success(request, "This Article Wasn't Saved")
        else:
            messages.warning(request, "This Article Doesn't Exists")
        return redirect("home")


# class CommentView(LoginRequiredMixin, View):
#     def post(self, request, article, *args, **kwargs):
#         form = CommentForm(request.POST)
#         if Article.objects.filter(id=article).exists():
#             articles = Article.objects.get(id=article)
#             if form.is_valid():
#                 Comment.objects.create(
#                     article=articles, author=request.user, content=form.cleaned_data.get("content"))
#                 return redirect("article-detail", article)
#             else:
#                 messages.warning(request, "Something Went Wrong")
#                 return redirect("article-detail", article)
#         else:
#             messages.warning(request, "Article Doesn't Exists")
#             return redirect("home")

class About(View):
    def get(self, request, *args, **kwargs):
        return render(request, "articles/about.html")


class Search(View):
    def get(self, request, *args, **kwargs):
        query = self.request.GET.get("q")
        if query == '' or query == ' ':
            messages.warning(request, "you can't search everything human!")
            return redirect("home")
        articles = Article.objects.filter(Q(title__icontains=query))
        return render(request, 'articles/search-results.html', {'results': articles, })


class AccountPage(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        savedarticles = Saved.objects.get(owner=request.user)
        context = {"saved": savedarticles.articles.all(), }
        return render(request, "articles/account.html", context)

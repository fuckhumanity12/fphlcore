from django.db import models
import uuid
from django.contrib.auth.models import User
from tinymce.models import HTMLField
from django.urls import reverse


class Subject(models.Model):
    id = models.UUIDField(editable=False, default=uuid.uuid4, primary_key=True)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Article(models.Model):
    id = models.UUIDField(editable=False, default=uuid.uuid4, primary_key=True)
    title = models.CharField(max_length=300)
    content = HTMLField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    description = models.CharField(max_length=500, blank=True, null=True)
    image = models.ImageField(upload_to='uploads/%Y/%m/%d/', null=True,)
    newsletter = models.BooleanField(default=True)
    subject = models.ForeignKey(
        Subject, on_delete=models.CASCADE)
    keywords = models.CharField(
        max_length=1000, default="forensic phonetics & linguistics, forensic phonetics, phonetics")
    lastmodified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("article-detail", kwargs={"pk": str(self.id)})


# class Comment(models.Model):
#     id = models.UUIDField(editable=False, default=uuid.uuid4, primary_key=True)
#     content = models.TextField()
#     author = models.ForeignKey(User, on_delete=models.CASCADE)
#     article = models.ForeignKey(
#         Article, on_delete=models.CASCADE, related_name="comments")
#     date = models.DateTimeField(auto_now_add=True)

#     class Meta:
#         ordering = ["-date"]

#     def __str__(self):
#         return self.content


class Saved(models.Model):
    id = models.UUIDField(editable=False, default=uuid.uuid4, primary_key=True)
    owner = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="savedarticles")
    articles = models.ManyToManyField(Article)

    def __str__(self):
        return self.owner.username

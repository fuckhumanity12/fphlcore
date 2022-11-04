from django.db import models
import uuid
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField


class Article(models.Model):
    id = models.UUIDField(editable=False, default=uuid.uuid4, primary_key=True)
    title = models.CharField(max_length=300)
    content = RichTextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    description = models.CharField(max_length=500, blank=True, null=True)
    image = models.ImageField(upload_to='uploads/%Y/%m/%d/', null=True,)

    def __str__(self):
        return self.title

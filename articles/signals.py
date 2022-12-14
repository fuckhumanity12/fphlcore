from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Saved, Article


@receiver(post_save, sender=User)
def create_saved(sender, instance, created, **kwargs):
    if created:
        Saved.objects.create(owner=instance)


@receiver(post_save, sender=Article)
def create_newsletter(sender, instance, created, **kwargs):
    if instance.newsletter:
        subject = f'New Article 🥳🥳: {instance.title}'
        emails = User.objects.filter(is_active=True).exclude(
            email='').exclude(is_active=False).values_list('email', flat=True)
        message = render_to_string(
            'articles/article-newsletter.html', {'article': instance, })
        for email in emails:
            send_mail(subject, message, "forensicphonetician@gmail.com",
                      [email], fail_silently=True)
    else:
        pass

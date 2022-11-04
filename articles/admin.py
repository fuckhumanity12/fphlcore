from django.contrib import admin
from .models import *
admin.site.register(Article)
admin.site.register(Saved)
# admin.site.register(Comment)
admin.site.site_header = "FPHL Administration"
admin.site.site_title = "FPHL Administration Panel"

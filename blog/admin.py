from django.contrib import admin
from .models import Blog

# Register your models here.


class BlogAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'body',
        'image',
        'date_added',
    )


admin.site.register(Blog, BlogAdmin)

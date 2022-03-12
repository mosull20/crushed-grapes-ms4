from django.contrib import admin
from .models import Review

# Register your models here.


class ReviewAdmin(admin.ModelAdmin):
    list_display = (
        'product',
        'user',
        'rating',
        'title',
        'description',
        'review_date',
    )
    ordering = ('product',)


admin.site.register(Review, ReviewAdmin)

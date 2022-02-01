from django import forms

from .models import Review


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('title', 'rating', 'description',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


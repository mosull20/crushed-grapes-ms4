from django import forms
from .widgets import CustomClearableFileInput
from .models import Blog


class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields =  ('title', 'body', 'image',)

    image = forms.ImageField(label='Image', required=False, widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

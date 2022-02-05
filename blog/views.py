from django.shortcuts import render


# Create your views here.
def blog(request):
    """ View to render the blog page """
    return render(request, 'blog/blog_page.html')

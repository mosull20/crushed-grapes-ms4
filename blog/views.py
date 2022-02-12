from django.shortcuts import render, get_object_or_404

from .models import Blog


# Create your views here.
def blog(request):
    """ View to render the blog page """
    blogs = Blog.objects.all()

    context = {
        'blogs': blogs,
    }
    return render(request, 'blog/blog_page.html', context)


def blog_detail(request, blog_id):
    """ 
    View to show individual blog posts
    """
    blog = get_object_or_404(Blog, pk=blog_id)
    
    context = {
        'blog': blog,
    }
    return render(request, 'blog/blog_detail.html', context)



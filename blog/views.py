from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import Blog
from .forms import BlogForm


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


@login_required
def add_blog(request):
    """ Add a blog post to the site """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners have access to this page.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            blog = form.save()
            messages.success(request, 'Successfully added a new blog post!')
            return redirect(reverse('blog_detail', args=[blog.id]))
        else:
            messages.error(request, 'Failed to add blog post. Please ensure form is correctly filled out.')
    else:
        form = BlogForm()

    template = 'blog/add_blog.html'
    context = {
        'form': form,
    }

    return render(request, template, context)

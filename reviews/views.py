from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from products.models import Product
from .models import Review
from .forms import ReviewForm


# Create your views here.
@login_required
def add_review(request, product_id):
    """ View to allow a user to add a review to a product """

    if not request.user.is_authenticated:
        messages.error(request, 'Sorry, only registered users can add reviews. \
            Please create an account or login to continue.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            title = request.POST.get('title')
            rating = request.POST.get('rating')
            description = request.POST.get('description')
            Review.objects.create(
                user=request.user,
                product=get_object_or_404(Product, pk=product_id),
                title=title,
                rating=rating,
                description=description,
            )
            messages.success(request, 'Successfully added review!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to add review. Please ensure \
                form is correctly filled out.')
    else:
        form = ReviewForm()

    template = 'reviews/add_review.html'
    context = {
        'form': form,
        'product': product
    }

    return render(request, template, context)

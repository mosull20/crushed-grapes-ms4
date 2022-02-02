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
        messages.info(request, f'You are adding a review for {product.name}')

    template = 'reviews/add_review.html'
    context = {
        'form': form,
        'product': product
    }

    return render(request, template, context)


@login_required
def edit_review(request, review_id):
    """ Allow a user to Edit their review """
    if not request.user.is_authenticated:
        messages.error(request, 'Sorry, only registered users can edit their reviews.')
        return redirect(reverse('home'))

    review = get_object_or_404(Review, pk=review_id)
    if request.method == 'POST':
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated review!')
            return redirect(reverse('product_detail', args=[review.product.id]))
        else:
            messages.error(request, 'Failed to update theis review. Please ensure form is correctly filled out.')
    else:
        form = ReviewForm(instance=review)
        messages.info(request, f'You are editing your review for {review.product.name}')

    template = 'reviews/edit_review.html'
    context = {
        'form': form,
        'product': review.product,
        'review': review,
    }

    return render(request, template, context)


@login_required
def delete_review(request, review_id):
    """ Allow a user to delete their review  """
    if not request.user.is_authenticated:
        messages.error(request, 'Sorry, only registered users can delete their reviews.')
        return redirect(reverse('home'))

    review = get_object_or_404(Review, pk=review_id)
    review.delete()
    messages.success(request, 'Your review has been deleted!')
    return redirect(reverse('products'))

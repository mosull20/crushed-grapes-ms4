from django.shortcuts import render

# Create your views here.

def view_cart(request):
    """ View to render the shopping cart contents page """
    
    return render(request, 'cart/cart.html')
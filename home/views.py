from django.shortcuts import render


def index(request):
    """ View to render the home page """
    return render(request, 'home/index.html')


def faqs(request):
    """ View to render the faqs page """
    return render(request, 'home/faqs.html')

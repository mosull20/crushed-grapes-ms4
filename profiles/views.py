from django.shortcuts import render


def profile(request):
    """ Display User's profile """

    template = 'profiles/profile.html'
    context = {

    }
    return render(request, template, context)

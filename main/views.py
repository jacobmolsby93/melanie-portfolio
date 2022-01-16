from django.shortcuts import render

# Create your views here.


def index(request):
    """
    A view to display home page.
    """

    return render(request, 'main/index.html')
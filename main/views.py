from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.core.paginator import Paginator
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponse
from .models import Image, PaintingImage
from .forms import ImageForm


# Create your views here.


def index(request):
    """
    A view to display home page.
    """

    return render(request, 'main/index.html')


def portfolio(request):
    """
    A view to display the portfolio
    """
    images = Image.objects.all().order_by("-created_on")

    paginator = Paginator(images, 12)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    on_page = True

    template_name = 'main/portfolio.html'
    context = {
        'on_page': on_page,
        'images': page_obj,

    }
    return render(request, template_name, context)


def paint_portfolio(request):
    """
    A view to display the portfolio
    """
    paintings = PaintingImage.objects.all().order_by("-created_on")

    paginator = Paginator(paintings, 12)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    on_page = True

    template_name = 'main/portfolio_2.html'
    context = {
        'on_page': on_page,
        'paintings': page_obj,

    }
    return render(request, template_name, context)



def about(request):
    """
    A view to display the about page
    """

    template_name = 'main/about.html'
    context = {

    }
    return render(request, template_name, context)
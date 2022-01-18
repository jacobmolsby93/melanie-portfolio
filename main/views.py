from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.core.paginator import Paginator
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponse
from .models import Image, PaintingImage
from .forms import ImageForm, PaintImageForm


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

    paginator = Paginator(images, 10)
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

    paginator = Paginator(paintings, 10)
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

def site_management(request):
    """
    A view to render management site.
    """

    images = Image.objects.all().order_by('-created_on')
    paintings = PaintingImage.objects.all().order_by('-created_on')

    template_name = 'main/site_management.html'
    context = {
        'images': images,
        'paintings': paintings,
    }
    return render(request, template_name, context)

# Views for normal photos

@login_required
def delete_image(request, image_id):
    """
    Delete an Image
    """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    image = get_object_or_404(Image, pk=image_id)
    image.delete()
    messages.success(request, 'Image deleted!')
    return redirect(reverse('portfolio'))

def add_image(request):
    """
    A view for adding images to the gallery
    """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save()
            messages.success(request, 'Successfully added Image!')
            return redirect(reverse('home'))
        else:
            messages.error(request, 'Failed to add Image. Please ensure the form is valid')
    else:
        form = ImageForm()
    template_name = 'main/add_image.html'
    context = {
        'form': form,
    }
    return render(request, template_name, context)


@login_required
def edit_image(request, image_id):
    """
    Edit a product in the store
    """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    image = get_object_or_404(Image, pk=image_id)

    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES, instance=image)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated image!')
            return redirect(reverse('home'))
        else:
            messages.error(request, 'Failed to update image. Please ensure the form is valid.')
    else:
        form = ImageForm(instance=image)
        messages.info(request, f'Your are editing {image.name}')
    
    template = 'main/edit_image.html'
    context = {
        'form': form,
        'image': image,
    }

    return render(request, template, context)

# Views for body paint images.

def add_painting(request):
    """
    A view for adding images to the gallery
    """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = PaintImageForm(request.POST, request.FILES)
        if form.is_valid():
            painting = form.save()
            messages.success(request, 'Successfully added Image!')
            return redirect(reverse('home'))
        else:
            messages.error(request, 'Failed to add Image. Please ensure the form is valid')
    else:
        form = PaintImageForm()
    template_name = 'main/add_painting.html'
    context = {
        'form': form,
    }
    return render(request, template_name, context)

@login_required
def delete_painting(request, painting_id):
    """
    Delete an Image
    """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    painting = get_object_or_404(PaintingImage, pk=painting_id)
    painting.delete()
    messages.success(request, 'Image deleted!')
    return redirect(reverse('home'))


@login_required
def edit_painting(request, painting_id):
    """
    Edit a product in the store
    """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    painting = get_object_or_404(PaintingImage, pk=painting_id)

    if request.method == 'POST':
        form = PaintImageForm(request.POST, request.FILES, instance=painting)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated image!')
            return redirect(reverse('home'))
        else:
            messages.error(request, 'Failed to update image. Please ensure the form is valid.')
    else:
        form = PaintImageForm(instance=painting)
        messages.info(request, f'Your are editing {painting.name}')
    
    template = 'main/edit_painting.html'
    context = {
        'form': form,
        'painting': painting,
    }

    return render(request, template, context)
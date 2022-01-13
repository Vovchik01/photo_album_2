from django.shortcuts import render, redirect
from .models import *


def index(request):
    category = request.GET.get('category')
    if category is None:
        images = Photo.objects.all()
    else:
        images = Photo.objects.filter(category__name=category)

    categories = Category.objects.all()
    context = {'categories': categories, 'images': images}
    return render(request, 'base/index.html', context)


def card_view(request, pk):
    image = Photo.objects.get(id=pk)
    context = {'image': image}
    return render(request, 'base/card_view.html', context)


def add_photo(request):
    categories = Category.objects.all()

    if request.method == "POST":
        data = request.POST
        image = request.FILES.get('img_upload')

        if data['category'] != 'none':
            category = Category.objects.get(id=data['category'])
        elif data['add_category'] != '':
            category, created = Category.objects.get_or_create(name=data['add_category'])
        else:
            category = None
        
        photo = Photo.objects.create(
            category=category,
            description=data['description'],
            image=image,
        )
        return redirect('index')

    context = {'categories': categories,}   
    return render(request, 'base/add_photo.html', context)
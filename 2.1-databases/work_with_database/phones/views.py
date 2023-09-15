from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Phone


def index(request):
    return redirect('catalog')

def show_catalog(request):
    template = 'phones/catalog.html'
    sort = request.GET.get('sort')
    if sort:
        if sort == 'name':
            phones = Phone.objects.order_by('name')
        elif sort == 'min_price':
            phones = Phone.objects.order_by('price')
        elif sort == 'max_price':
            phones = Phone.objects.order_by('-price')
    else:
        phones = Phone.objects.all()
    context = {'phones': phones}
    return render(request, template, context)

def show_product(request, slug):
    template = 'phones/product.html'
    phone = Phone.objects.get(slug=slug)
    context = {'phone': phone}
    return render(request, template, context)

# def show_product(request, slug):
#     template = 'phones/product.html'
#     phone = Phone.objects.get(name=slug)
#     context = {'phone': phone}
#     return render(request, template, context)



# def show_product(request, phone_id):
#     template = 'phones/product.html'
#     phone = Phone.objects.get(id=phone_id)
#     context = {'phone': phone}
#     return render(request, template, context)




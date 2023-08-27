from django.shortcuts import render
from django.http import HttpResponse


DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
}

def say_hello(request, name):
    resp = 'Hello, {}!'.format(name)
    context = {
        'answer': resp
    }
    return render(request, 'calculator/greeting.html', context)

def get_products(request, food):
    quantity = request.GET.get('servings')
    context = {}
    products = {}
    if food in DATA:
        products = DATA[food].copy()
    if quantity:
        quantity = int(quantity)
        if products:
            for ingr in products:
                products[ingr] = round(products[ingr] * quantity, 3)
    if products:
        context = {
                    'food': products
                }
    
    return render(request, 'calculator/products.html', context)


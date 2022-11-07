from django.shortcuts import render
from .models import Product

# Create your views here.


def products(request):
    """ a view to return shop page"""

    products = Product.objects.all()

    context = {
        'products': products,
    }

    return render(request, 'products/products.html', context)

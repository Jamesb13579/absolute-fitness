from django.shortcuts import render
from .models import Product, Memberships

# Create your views here.


def products(request):
    """ a view to return shop page"""

    products = Product.objects.all()

    context = {
        'products': products,
    }

    return render(request, 'products/products.html', context)


def memberships(request):
    """ a view to return shop page"""

    memberships = Memberships.objects.all()

    context = {
        'memberships': memberships,
    }

    return render(request, 'products/memberships.html', context)
from django.shortcuts import render, get_object_or_404
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
    """ a view to return membership options"""

    memberships = Memberships.objects.all()

    context = {
        'memberships': memberships,
    }

    return render(request, 'products/memberships.html', context)


def product_detail(request, product_id):
    """ a view to show individial item details"""

    product = get_object_or_404(Product, pk=product_id)
    
    context = {
        'product': product,
        
    }

    return render(request, 'products/product_detail.html', context)


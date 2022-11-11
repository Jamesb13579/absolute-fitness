from django.shortcuts import render, get_object_or_404
from .models import Product, Memberships

# Create your views here.


def products(request):
    """ a view to return shop page"""
    products = Product.objects.all()
    membership = None
    if request.GET:
        if 'membership' in request.GET:
            memberships = request.GET['membership'].split(',')
            products = products.filter(membership__name__in=memberships)
            memberships = Memberships.objects.filter(name__in=memberships)

    context = {
        'products': products,
    }

    return render(request, 'products/products.html', context)


def category(request):
    """ a view to return membership options"""

    category = Category().objects.all()

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




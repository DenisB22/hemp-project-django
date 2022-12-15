from django.shortcuts import render

from final_project.accounts.models import Account
from final_project.category.models import Category
from final_project.store.models import Product, ReviewRating


# Create your views here.



def get_products():
    return Product.objects.all().filter(is_available=True).order_by('created_date')


def home(request):

    products = get_products()
    reviews = None

    # Get the reviews
    for product in products:
        reviews = ReviewRating.objects.filter(product_id=product.id, status=True)

    context = {
        'products': products,
        'reviews': reviews,
    }
    return render(request, 'core/home.html', context)

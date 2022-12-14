from django.contrib import messages
from django.core.paginator import Paginator
from django.http import HttpResponse
from rest_framework import serializers
from rest_framework import generics as rest_views
from rest_framework import views  as rest_base_views
from rest_framework import viewsets

from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from rest_framework.response import Response

from final_project.carts.models import CartItem
from final_project.carts.views import _cart_id
from final_project.category.models import Category
from final_project.orders.models import OrderProduct
from final_project.store.forms import ReviewForm

from final_project.store.models import Product, ReviewRating, ProductGallery
from final_project.store.serializers import CategorySerializer, ProductSerializer, ShortProductSerializer, \
    ShortCategorySerializer


# Create your views here

def store(request, category_slug=None):
    category = None
    products = None
    page_obj = None

    if category_slug != None:
        category = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category=category, is_available=True).order_by('id')
        products_count = products.count()
    else:

        products = Product.objects.all().filter(is_available=True)
        products_count = products.count()

        # paginator = Paginator(products, 6)
        # page_number = request.GET.get('page')
        # page_obj = paginator.get_page(page_number)

    paginator = Paginator(products, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'products': page_obj,
        'products_count': products_count,
        # 'page_obj': page_obj,
    }
    return render(request, 'store/store.html', context)


class CategoriesListApiView(rest_views.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


# JSON serialization, i.e. parse models into JSON
class ProductsListApiView(rest_views.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_queryset(self):
        category_id = self.request.query_params.get('category_id')
        queryset = self.queryset
        if category_id:
            queryset = queryset.filter(category_id=category_id)
        return queryset.all()


class NameSerializer(serializers.Serializer):
    category_name = serializers.CharField()


class DemoSerializer(serializers.Serializer):
    products = ShortProductSerializer(many=True)
    products_count = serializers.IntegerField()
    categories = ShortCategorySerializer(many=True)
    first_category = serializers.CharField()
    category_names = NameSerializer(many=True)


class DemoApiView(rest_base_views.APIView):
    def get(self, request):
        products = Product.objects.all()
        categories = Category.objects.all()
        body = {
            'products': products,
            'products_count': products.count(),
            'categories': categories,
            'first_category': categories.first(),
            'category_names': categories,
        }

        serializers = DemoSerializer(body)

        return Response(serializers.data)


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


def product_details(request, category_slug, product_slug):
    is_oil = False

    try:
        product = Product.objects.get(category__slug=category_slug, slug=product_slug)
        in_cart = CartItem.objects.filter(cart__cart_id=_cart_id(request), product=product).exists()
        if 'cbd-oil' in product_slug:
            is_oil = True
    except Exception as e:
        raise e

    if request.user.is_authenticated:
        try:
            orderproduct = OrderProduct.objects.filter(user=request.user, product_id=product.id).exists()
        except OrderProduct.DoesNotExist:
            orderproduct = None
    else:
        orderproduct = None

    # Get the reviews
    reviews = ReviewRating.objects.filter(product_id=product.id, status=True)

    # Get the product gallery
    product_gallery = ProductGallery.objects.filter(product_id=product.id)

    context = {
        'product': product,
        'in_cart': in_cart,
        'orderproduct': orderproduct,
        'reviews': reviews,
        'product_gallery': product_gallery,

    }
    return render(request, 'products/product-detail.html', context)


def product_search(request):
    products = None
    products_count = 0

    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            products = Product.objects.order_by('-created_date').filter(Q(description__icontains=keyword) | Q(product_name__icontains=keyword))
            products_count = products.count()

    context = {
        'products': products,
        'products_count': products_count,
    }

    return render(request, 'store/store.html', context)


def submit_review(request, product_id):
    url = request.META.get('HTTP_REFERER')
    if request.method == 'POST':
        try:
            reviews = ReviewRating.objects.get(user__id=request.user.id, product__id=product_id)
            form = ReviewForm(request.POST, instance=reviews)
            form.save()
            messages.success(request, 'Thank you! Your review has been updated.')
            return redirect(url)
        except ReviewRating.DoesNotExist:
            form = ReviewForm(request.POST)
            if form.is_valid():
                data = ReviewRating()
                data.subject = form.cleaned_data['subject']
                data.rating = form.cleaned_data['rating']
                data.review = form.cleaned_data['review']
                data.ip = request.META.get('REMOTE_ADDR')
                data.product_id = product_id
                data.user_id = request.user.id
                data.save()
                messages.success(request, 'Thank you! Your review has been submitted.')
                return redirect(url)


def about_page(request):
    return render(request, 'core/about.html')
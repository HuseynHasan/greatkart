from django.shortcuts import render, get_object_or_404
# from carts.models import CartItem
from category.models import Category
from store.models import Product
# from carts.views import _cart_id
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.db.models import Q


# Create your views here.


def store(request, category_slug=None):
    products = Product.objects.filter(is_available=True)

    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)

    products = products.order_by('id')
    product_count = products.count()

    context = {
        'products': products,
        'product_count': product_count,
    }

    return render(request, 'store/store.html', context)


# #https://chatgpt.com/s/t_697c6cddce2481918ee47e95c9a123c0
def product_detail(request, category_slug, product_slug):

    single_product = get_object_or_404(
        Product, 
        category_slug=category_slug, 
        slug=product_slug
        )

        # in_cart = CartItem.objects.filter(cart__cart_id=_cart_id(request), product=single_product).exists()

    context = {
        "single_product":single_product,
        # "in_cart"       :in_cart,
    }
    return render(request, 'store/product-detail.html', context)


# def search(requset):
#     if 'keyword' in requset.GET:
#         keyword = requset.GET['keyword']
#         if keyword:
#             products = Product.objects.order_by('-created_date').filter(Q(description__icontains=keyword) | Q(product_name__icontains=keyword))
#             product_count = products.count()
#     context = {
#         'products':products,
#         'product_count':product_count,
#         }
#     return render(requset, 'store/store.html', context)

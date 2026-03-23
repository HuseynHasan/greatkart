from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.shortcuts import redirect, render, get_object_or_404
from carts.models import Cart, CartItem
from store.models import Product
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.

def _cart_id(request):
    if not request.session.session_key:
        request.session.create()
    return request.session.session_key


def add_cart(request, product_id):
    # product = Product.objects.get(id=product_id)
    product = get_object_or_404(Product, id=product_id)

    cart, _ = Cart.objects.get_or_create(
        cart_id=_cart_id(request)
    )

    cart_item, created = CartItem.objects.get_or_create(
        product=product,
        cart=cart,
        defaults={'quantity': 1}
    )

    if not created:
        cart_item.quantity += 1
        cart_item.save(update_fields=['quantity'])

    return redirect('cart')


def remove_cart(request, product_id):
    cart_id = _cart_id(request)

    cart_item = CartItem.objects.filter(
        cart__cart_id=cart_id,
        product_id=product_id
    ).first()

    if not cart_item:
        return redirect('cart')

    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save(update_fields=['quantity'])
    else:
        cart_item.delete()

    return redirect('cart')


def remove_cart_item(request, product_id):
    CartItem.objects.filter(
        cart__cart_id=_cart_id(request),
        product_id=product_id
    ).delete()

    return redirect('cart')



def cart(request):
    total = 0
    quantity = 0

    cart_items = CartItem.objects.filter(
        cart__cart_id=_cart_id(request),
        is_active=True
    ).select_related('product')

    for item in cart_items:
        total += item.product.price * item.quantity
        quantity += item.quantity

    tax = (2 * total) / 100
    grand_total = total + tax

    return render(request, 'store/cart.html', {
        'total': total,
        'quantity': quantity,
        'cart_items': cart_items,
        'tax': tax,
        'grand_total': grand_total,
    })
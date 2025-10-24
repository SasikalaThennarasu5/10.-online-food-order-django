from django.shortcuts import render, get_object_or_404, redirect
from .models import MenuItem, Category
from django.http import JsonResponse
from django.views.decorators.http import require_POST

def home(request):
    featured = MenuItem.objects.filter(is_featured=True)[:6]
    categories = Category.objects.all()
    return render(request, 'home.html', {'featured': featured, 'categories': categories})

def menu(request):
    items = MenuItem.objects.all()
    categories = Category.objects.all()
    return render(request, 'menu.html', {'items': items, 'categories': categories})

def item_detail(request, item_id):
    item = get_object_or_404(MenuItem, id=item_id)
    return render(request, 'item_detail.html', {'item': item})

def cart_view(request):
    # simple cart stored in session as {item_id: qty}
    cart = request.session.get('cart', {})
    items = []
    total = 0
    for item_id, qty in cart.items():
        try:
            mi = MenuItem.objects.get(id=item_id)
            subtotal = mi.price * qty
            items.append({'item': mi, 'qty': qty, 'subtotal': subtotal})
            total += subtotal
        except MenuItem.DoesNotExist:
            pass
    return render(request, 'cart.html', {'cart_items': items, 'total': total})

@require_POST
def add_to_cart(request, item_id):
    cart = request.session.get('cart', {})
    cart[str(item_id)] = cart.get(str(item_id), 0) + 1
    request.session['cart'] = cart
    return redirect('cart')

def checkout(request):
    if request.method == 'POST':
        # very simple checkout: create order record (no payment integration)
        from .models import Order, OrderItem, MenuItem
        data = request.POST
        order = Order.objects.create(full_name=data.get('full_name'),
                                     email=data.get('email'),
                                     address=data.get('address'),
                                     paid=False)
        cart = request.session.get('cart', {})
        for item_id, qty in cart.items():
            mi = MenuItem.objects.get(id=item_id)
            OrderItem.objects.create(order=order, menu_item=mi, quantity=qty)
        request.session['cart'] = {}
        return render(request, 'order_success.html', {'order': order})
    return render(request, 'checkout.html')

def restaurant_dashboard(request):
    # placeholder admin-like dashboard for restaurants (no auth required in scaffold)
    categories = Category.objects.all()
    items = MenuItem.objects.all()
    return render(request, 'dashboard.html', {'categories': categories, 'items': items})

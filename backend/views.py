from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Product, Category, Order, OrderItem

def product_list(request):
    products = Product.objects.all()
    categories = Category.objects.all()
    return render(request, 'products/product_list.html', {'products': products, 'categories': categories})

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'products/product_detail.html', {'product': product})

@login_required
def cart(request):
    order, created = Order.objects.get_or_create(user=request.user, completed=False)
    items = order.items.all()
    return render(request, 'orders/cart.html', {'items': items, 'order': order})

@login_required
def add_to_cart(request, pk):
    product = get_object_or_404(Product, pk=pk)
    order, created = Order.objects.get_or_create(user=request.user, completed=False)
    order_item, created = OrderItem.objects.get_or_create(order=order, product=product, defaults={'quantity': 1, 'price': product.price})
    if not created:
        order_item.quantity += 1
        order_item.save()
    return redirect('cart')

@login_required
def remove_from_cart(request, pk):
    order_item = get_object_or_404(OrderItem, pk=pk)
    order_item.delete()
    return redirect('cart')

@login_required
def checkout(request):
    order, created = Order.objects.get_or_create(user=request.user, completed=False)
    if request.method == 'POST':
        order.completed = True
        order.save()
        return redirect('orders:order_list')
    return render(request, 'orders/checkout.html', {'order': order})
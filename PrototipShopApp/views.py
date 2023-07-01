from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from .models import Product
from .models import ShoppingCart

# Create your views here.
def home(request):

    if request.user.is_authenticated:
        productsOnFireQuerySet = Product.objects.filter(category__name="Unisex").order_by('?')[:3]

        context = {"products": productsOnFireQuerySet,}
        return render(request,"home.html",context=context)
    else:
        return redirect('admin:index')

@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, pk=product_id)

    cart, created = ShoppingCart.objects.get_or_create(user=request.user)

    cart.products.add(product)

    print(f"Product '{product.name}' added to cart for user '{request.user.username}'")

    return redirect('view_cart')

@login_required
def remove_from_cart(request, product_id):
    product = get_object_or_404(Product, pk=product_id)

    cart, created = ShoppingCart.objects.get_or_create(user=request.user)

    cart.products.remove(product)

    print(f"Product '{product.name}' removed from cart for user '{request.user.username}'")

    return redirect('view_cart')

def view_cart(request):
    cart = ShoppingCart.objects.get(user=request.user)

    products = cart.products.all()

    total_sum = sum(product.price * (100 - product.sale) / 100 for product in products)

    total_sum = round(total_sum)

    context = {'cart': cart, 'products': products, 'sum':total_sum}
    return render(request, 'cart.html', context)

def redirect_to_home(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        return redirect('root')

def view_all_products(request):

    allProducts = Product.objects.all()

    context = {"allProducts" : allProducts}
    return render(request,'products.html',context=context)

def make_payment(request):
    return render(request,"payment.html")

def simulate_payment(request):
    cart = get_object_or_404(ShoppingCart, user=request.user)
    cart.products.all().delete()
    return render(request,'simulatepayment.html')

def logout_view(request):
    logout(request)
    return redirect('admin:index')



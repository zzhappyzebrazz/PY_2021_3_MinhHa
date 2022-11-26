from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'store/index.html')

def cart(request):
    return render(request, 'store/cart.html')

def checkout(request):
    return render(request, 'store/checkout.html')

def contact(request):
    return render(request, 'store/contact.html')

def login(request):
    return render(request, 'store/login.html')

def my_account(request):
    return render(request, 'store/my_account.html')

def product_detail(request):
    return render(request, 'store/product_detail.html')

def product_list(request):
    return render(request, 'store/product_list.html')

def wishlist(request):
    return render(request, 'store/wishlist.html')

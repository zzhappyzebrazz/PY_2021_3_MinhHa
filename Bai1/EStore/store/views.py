from django.shortcuts import render
from store.models import *

#all products
all_products = Product.objects.all()
sub_category_1_list = [1, 2, 3, 4, 5]
sub_category_2_list = [6, 7, 8, 9, 10]
# Create your views here.
def index(request):
    #Slider
    sliders = Slider.objects.all()
    print(sliders)

    #Brands
    brands = Brand.objects.all()
    print(brands)


    #Thiết bị gia đình
    sub_category_1 = [product for product in all_products if product.subcategory_id in sub_category_1_list]
    print(f'Số lượng sản phẩm trong Thiết bị gia đình {len(sub_category_1)}')

    #Đồ dùng nhà bếp
    sub_category_2 = [product for product in all_products if product.subcategory_id in sub_category_2_list]
    print(f'Số lượng sản phẩm trong Đồ dùng nhà bếp {len(sub_category_2)}')

    return render(request, 'store/index.html',{
        'sub_category_1' : sub_category_1,
        'sub_category_2' : sub_category_2,
        'sliders' : sliders,
        'brands' : brands,
    })

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

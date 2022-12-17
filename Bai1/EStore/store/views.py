from unicodedata import category
from django.shortcuts import render
from store.models import *
from django.core.paginator import Paginator
from store.forms import *

#all products
# all_products = Product.objects.all()
# sub_category_1_list = [1, 2, 3, 4, 5]
# sub_category_2_list = [6, 7, 8, 9, 10]

# Create your views here.
def index(request):
    #Slider
    sliders = Slider.objects.all()
    print(sliders)

    #Brands
    brands = Brand.objects.all()
    print(brands)


    #Thiết bị gia đình
    # sub_category_1 = [product for product in all_products if product.subcategory_id in sub_category_1_list]
    sub_category_1 = SubCategory.objects.filter(category=1).values_list('id')
    list_subcategory_1 = [sub_category_1[0] for sub_category_1 in sub_category_1]
    product_subcategory_1 = Product.objects.filter(subcategory__in=list_subcategory_1).order_by('-public_day')[:20]
    print(f'Số lượng sản phẩm trong Thiết bị gia đình {len(product_subcategory_1)}')

    sub_category_2 = SubCategory.objects.filter(category=2).values_list('id')
    list_subcategory_2 = [sub_category_2[0] for sub_category_2 in sub_category_2]
    product_subcategory_2 = Product.objects.filter(subcategory__in=list_subcategory_2).order_by('-public_day')[:20]
    print(f'Số lượng sản phẩm trong Thiết bị gia đình {len(product_subcategory_2)}')

    #Đồ dùng nhà bếp
    # sub_category_2 = [product for product in all_products if product.subcategory_id in sub_category_2_list]
    # print(f'Số lượng sản phẩm trong Đồ dùng nhà bếp {len(sub_category_2)}')

    return render(request, 'store/index.html',{
        'product_subcategory_1' : product_subcategory_1,
        'product_subcategory_2' : product_subcategory_2,
        'sliders' : sliders,
        'brands' : brands,
    })



# Create your views here.
def index_2(request):
    #Slider
    sliders = Slider.objects.all()
    print(sliders)

    #Brands
    brands = Brand.objects.all()
    print(brands)


    #Thiết bị gia đình
    # sub_category_1 = [product for product in all_products if product.subcategory_id in sub_category_1_list]
    sub_category_1 = SubCategory.objects.filter(category=1).values_list('id')
    list_subcategory_1 = [sub_category_1[0] for sub_category_1 in sub_category_1]
    product_subcategory_1 = Product.objects.filter(subcategory__in=list_subcategory_1).order_by('-public_day')[:20]
    print(f'Số lượng sản phẩm trong Thiết bị gia đình {len(product_subcategory_1)}')

    sub_category_2 = SubCategory.objects.filter(category=2).values_list('id')
    list_subcategory_2 = [sub_category_2[0] for sub_category_2 in sub_category_2]
    product_subcategory_2 = Product.objects.filter(subcategory__in=list_subcategory_2).order_by('-public_day')[:20]
    print(f'Số lượng sản phẩm trong Thiết bị gia đình {len(product_subcategory_2)}')

    #Đồ dùng nhà bếp
    # sub_category_2 = [product for product in all_products if product.subcategory_id in sub_category_2_list]
    
    dem = 0
    print('======================================')
    print(request.COOKIES.get('so_lan_truy_cap'))
    print('======================================')
    if request.COOKIES.get('so_lan_truy_cap') is not None:
        print('You are here')
        print(dem)
        dem = int(request.COOKIES.get('so_lan_truy_cap')) + 1
        print(dem)

    response = render(request, 'store/index.html',{
        'product_subcategory_1' : product_subcategory_1,
        'product_subcategory_2' : product_subcategory_2,
        'sliders' : sliders,
        'brands' : brands,
    })

    response.set_cookie('so_lan_truy_cap', dem)

    return response

def subcategory(request, pk):
    sub_category = SubCategory.objects.order_by('name')
    headline = ''
    if pk == 0:
        products_list = Product.objects.order_by('-public_day')[:150]
        headline = 'Tất cả sản phẩm (' + str(products_list.count()) + ')'
    else:
        products_list = Product.objects.filter(subcategory=pk)
        for category in sub_category:
            if category.id == pk:
                headline = str(category.name) + ' (' + str(products_list.count()) +')'
        # headline = 'Tất cả sản phẩm (' + str(products.count()) + ')'
    
    print(headline)

    page = request.GET.get('page', 1) # Trang bắt đầu
    paginator = Paginator(products_list, 15) #Số items trên 1 page
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)                 

    #Brands
    brands = Brand.objects.all()
    
    return render(request, 'store/product_list.html',{
        'headline' : headline,
        'products' : products,
        'products_list' : products_list,
        'sub_category' : sub_category,
        'brands' : brands,
    })

def product_detail(request, pk):
    product = Product.objects.get(pk=pk)
    sub_category = SubCategory.objects.order_by('name')
    product_category = ''
    for category in sub_category:
        if category.id == product.subcategory_id:
            product_category = category
    related_product = Product.objects.filter(subcategory_id=product.subcategory_id)
    # print(related_product)
    print(product_category)
    
    brands = Brand.objects.all()
    
    return render(request, 'store/product_detail.html', {
        'sub_category' : sub_category,
        'product_category' : product_category,
        'related_product' : related_product,
        'product' : product,
        'brands' : brands,
    })

def search(request):
    return render(request, 'store/product_list.html')

def cart(request):
    return render(request, 'store/cart.html')

def checkout(request):
    return render(request, 'store/checkout.html')

def contact(request):
    return render(request, 'store/contact.html')

def demo_auth_user(request):
    result_register = ''
    form_user = FormUser()
    form_profile = FormUserProfileInfo()

    if request.POST.get('username'):
        form_user = FormUser(data=request.POST)
        form_user_profile = FormUserProfileInfo(data=request.POST)
        if form_user.is_valid() and form_user_profile.is_valid():
            if form_user.cleaned_data['password'] == form_user.cleaned_data['confirm_password']:
                #User
                user = form_user.save()
                user.set_password(user.password)
                user.save()

                #Profile
                profile = form_user_profile.save(commit=False)
                profile.user = user
                profile.portfolio = form_user_profile.cleaned_data['portfolio']
                if 'image' in request.FILES:
                    profile.image = request.FILE['image']
                profile.save()

                print(user)
                result_register = '''
                        <div class="alert alert-success" role="alert">
                            Đang ký thành công!
                        </div>
                        '''
            else:
                result_register = '''
                <div class="alert alert-danger" role="alert">
                    Xác nhận mật khẩu không thành công
                </div>
                '''
        else:
            print('you are here')
            result_register = '''
            <div class="alert alert-danger" role="alert">
                Đăng ký không thành công
            </div>
            '''


    return render(request, 'store/auth_user.html',{
        'form_user': form_user,
        'form_profile' : form_profile,
        'result_register' : result_register,
    })

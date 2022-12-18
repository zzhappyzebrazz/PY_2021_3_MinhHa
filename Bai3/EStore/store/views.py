from unicodedata import category
from django.shortcuts import render
from store.models import *
from django.core.paginator import Paginator
from store.forms import *
from django.db.models import Q

brands = Brand.objects.all()
sub_category = SubCategory.objects.order_by('name')

# Create your views here.
def index_2(request):
    #Slider
    sliders = Slider.objects.all()
    print(sliders)
    
    print(brands)
    #Thiết bị gia đình
    sub_category_1 = SubCategory.objects.filter(category=1).values_list('id')
    list_subcategory_1 = [sub_category_1[0] for sub_category_1 in sub_category_1]
    product_subcategory_1 = Product.objects.filter(subcategory__in=list_subcategory_1).order_by('-public_day')[:20]
    print(f'Số lượng sản phẩm trong Thiết bị gia đình {len(product_subcategory_1)}')
    
    #Đồ dùng nhà bếp
    sub_category_2 = SubCategory.objects.filter(category=2).values_list('id')
    list_subcategory_2 = [sub_category_2[0] for sub_category_2 in sub_category_2]
    product_subcategory_2 = Product.objects.filter(subcategory__in=list_subcategory_2).order_by('-public_day')[:20]
    print(f'Số lượng sản phẩm trong Thiết bị gia đình {len(product_subcategory_2)}')

    
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

def paginator(request, all_product, num_of_items):
    page = request.GET.get('page', 1) # Trang bắt đầu
    paginator = Paginator(all_product, num_of_items) #Số items trên 1 page
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)   
    
    return products

def subcategory(request, pk):
    headline = ''
    should_show_filter = True

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
    if request.method == "GET":
        if request.GET.get("from_price"):
            from_price = int(request.GET.get("from_price"))
            to_price = int(request.GET.get("to_price"))
            # product_name = request.GET.get("product_name")
            filter_result = filter(products_list, from_price, to_price)
            num_of_items = 15
            print(len(filter_result))
            headline = 'Tìm thấy ' + str(len(filter_result)) + ' sản phẩm'

    num_of_items = 15
    products = paginator(request, products_list, num_of_items)
    
    return render(request, 'store/product_list.html',{
        'should_show_filter' : should_show_filter,
        'headline' : headline,
        'products' : products,
        'products_list' : products_list,
        'sub_category' : sub_category,
        'brands' : brands,
    })

def product_detail(request, pk):
    
    product = Product.objects.get(pk=pk)
    product_category = ''
    for category in sub_category:
        if category.id == product.subcategory_id:
            product_category = category
    related_product = Product.objects.filter(subcategory_id=product.subcategory_id)
    # print(related_product)
    print(product_category)
    
    return render(request, 'store/product_detail.html', {
        'sub_category' : sub_category,
        'product_category' : product_category,
        'related_product' : related_product,
        'product' : product,
        'brands' : brands,
    })

def filter(product_list, from_price, to_price):
    products = []
    if to_price > from_price:
        for product in product_list:
            if product.price in range(from_price, to_price):
                products.append(product)
                
    print(products)
    return products

def search(request):
    input_search = ''
    url_search = ''
    headline = ''
    products = ''
    should_show_filter = False
    
    if request.method == "GET":
        if request.GET.get("all_search"):
            input_search = request.GET.get("all_search")
            print(input_search)
            result_search = Product.objects.filter(
                Q(name__contains=input_search)
            ).order_by("name")
            print(result_search)
            num_of_items = 15
            products = paginator(request, result_search, num_of_items)
            # print(prod
            headline = 'Tìm thấy ' + str(result_search.count()) + ' sản phẩm'
            url_search = '&all_search=' + input_search
            if result_search.count() > 1:
                should_show_filter = True
        else:
            print("Could not get input_search")
            
    if request.method == "GET":
        if request.GET.get("from_price"):
            from_price = int(request.GET.get("from_price"))
            to_price = int(request.GET.get("to_price"))
            product_name = request.GET.get("product_name")
            produt_list = Product.objects.filter(Q(name__contains=product_name)).order_by("name")
            result_search = filter(produt_list, from_price, to_price)
            num_of_items = 15
            print(len(result_search))
            if len(result_search) > 1:
                should_show_filter = True
            headline = 'Tìm thấy ' + str(len(result_search)) + ' sản phẩm'
            products = paginator(request, result_search, num_of_items)

            
    return render(request, 'store/product_list.html', {
        'headline' : headline,
        'should_show_filter' : should_show_filter,
        'input_search' : input_search,
        'products' : products,
        'url_search' : url_search,
        'sub_category' : sub_category,
        'brands' : brands,
    })

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

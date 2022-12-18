from django.shortcuts import render, redirect
from customer.models import Customer
from customer.forms import FormDangKy
from django.contrib.auth.hashers import PBKDF2PasswordHasher, Argon2PasswordHasher

# Create your views here.
def login(request):
    #Define hasher to use
    hasher = PBKDF2PasswordHasher()

    # TRẠNG THÁI ĐĂNG NHẬP
    if 's_user' in request.session:
        return redirect('store:index_2')

    #THỤC HIỆN CHỨC NĂNG ĐĂNG NHẬP
    result_login = ''
    if request.POST.get('login_email'):
        login_email = request.POST.get('login_email')
        login_password = request.POST.get('login_password')
        print('=====================')
        print(login_email)
        print(hasher.encode(login_password, 'magic string'))
        print('=====================')
        query = Customer.objects.filter(email=login_email, password=hasher.encode(login_password, 'magic string'))
        print(query)
        if query.count() > 0:
            print(type(query))
            dict_user = query.values()[0]
            print(type(query.values()))
            print(type(dict_user))
            print(dict_user)
            del(dict_user['password'])
            print(dict_user)
            request.session['s_user'] = dict_user
            result_login = '''
                    <div class="alert alert-success" role="alert">
                        Đăng nhập thành công!
                    </div>
                    '''
            return redirect('store:index_2')
        else:
            result_login = '''
                    <div class="alert alert-danger" role="alert">
                        Đang nhập thất bại!
                    </div>
                    '''


    #THỰC HIỆN CHỨC NĂNG ĐĂNG KÝ
    form = FormDangKy()
    result_register = ''
    if request.POST.get('first_name'):
        form = FormDangKy(request.POST, Customer)
        if form.is_valid():
            print('Get valid POST from CUSTOMER')
            if form.cleaned_data['password'] == form.cleaned_data['confirm_password']:
                request.POST._mutable = True
                post = form.save(commit=False)
                post.first_name = form.cleaned_data['first_name']
                post.last_name = form.cleaned_data['last_name']
                post.email = form.cleaned_data['email']
                post.password = hasher.encode(form.cleaned_data['password'], 'magic string')
                #<algorithm>$<iterations>$<salt>$<hash>
                post.phone = form.cleaned_data['phone']
                post.address = form.cleaned_data['address']
                post.save()

                result_register = '''
                        <div class="alert alert-success" role="alert">
                            Đang ký thành công!
                        </div>
                        '''
            else:
                print('CONFIRM PASSWORD NOT MATCH')
                result_register = '''
                        <div class="alert alert-danger" role="alert">
                            Xác nhận mật khẩu không thành công
                        </div>
                        '''
    
        else:
            result_register = '''
            <div class="alert alert-danger" role="alert">
                Đăng ký không thành công
            </div>
            '''

    return render(request, 'store/login.html',{
        'result_register' : result_register,
        'result_login' : result_login,
        'form' : form,
    })

def my_account(request):
    # return render(request, 'store/my_account.html')
    if 's_user' in request.session:
        user = request.session['s_user']
        print(user)
        return render(request, 'store/my_account.html', {
            'user' : user,
        })
    else:
        print('User unregisterd')
        return redirect('store:index_2')

def log_out(request):
    if 's_user' in request.session:
        del request.session['s_user']
        print(request.session)
        print("=========================")
    return redirect('customer:login')


from ast import Pass
from audioop import add
from cProfile import Profile
import email
import imp
from itertools import product
from math import prod
from statistics import quantiles
from unicodedata import category, name
import uuid
from django.shortcuts import render, redirect
from django.shortcuts import HttpResponse
from requests import request
from accounts.models import Accounts, Wallet, WalletTransactions
from django.contrib.auth import authenticate
from django.contrib.auth import logout, login
from django.contrib import messages
from adminapp.models import Category, Coupen, Product, user_coupon
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_control
from .models import Address, OrderItem, OrderTable
from django.views.decorators.csrf import csrf_exempt
from userapp.twilio import MessageHandler
from django.db.models import Q
from django.core.exceptions import ObjectDoesNotExist
from adminapp.views import customers
from .models import Cart
import json
from django.http import JsonResponse
import razorpay
from django.core.paginator import Paginator, EmptyPage


# Create your views here.


def landing(request):
    return redirect(shop)


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def user_home(request):
    category = Category.objects.all()
    if 'user_id' in request.session:
        product = Product.objects.all()
        log = True
        return render(request, 'user/index.html', {'log': log, "product": product, 'category': category})
    else:
        product = Product.objects.all()
        log = False
        return render(request, 'user/index.html', {"product": product, 'category': category, 'log': log})


# def user_login(request):

#     return render(request, 'user/user_login.html')    

def user_signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        phone = request.POST['phone']
        password = request.POST['pass1']
        password2 = request.POST['pass2']

        if password == password2 and len(password) >= 5:
            try:
                k = int(request.POST['phone'])
            except:
                messages.error(request, 'Please enter the phone Number', extra_tags='signphone_number')
                return redirect(user_signup)
            if username == '' or email == '' or phone == '' or password == '' or password2 == '':
                messages.error(request, 'Username must not be empty', extra_tags='signusername')
                messages.error(request, 'Email must not be empty', extra_tags='signemail')
                messages.error(request, 'Password must not be empty', extra_tags='signpass')
                messages.error(request, 'Phone number must not be empty', extra_tags='signphone_number')
                return redirect(user_signup)
            elif len(phone) != 10:
                messages.error(request, 'Enter corrrect phone number', extra_tags='signphone_number')
                return redirect(user_signup)
            elif Accounts.objects.filter(username=username):
                messages.error(request, 'username already  exists', extra_tags='signusername')
                return redirect(user_signup)
            elif Accounts.objects.filter(email=email):
                messages.error(request, 'Email already  exists', extra_tags='signemail')
                return redirect(user_signup)
            elif Accounts.objects.filter(phone=phone):
                messages.error(request, 'Phone number already  exists', extra_tags='signphone_number')
                return redirect(user_signup)
            else:
                if Accounts.objects.filter(username=username):
                    messages.error(request, 'Username already exists', extra_tags='signusername')
                    return redirect(user_signup)
                else:
                    account = Accounts.objects.create_user(
                        username=username,
                        first_name=first_name,
                        last_name=last_name,
                        email=email,
                        phone=phone,
                        password=password
                    )

                    account.save()
                    messages.success(request, "User Created Successfully")
                    # request.session['user_id'] = username
                    # number = "+91" + phone
                    # if SendOTP(number):
                    #     item.save()
                    # return render(request, 'user/otp.html')
        else:
            messages.error(request, '''Password must be same 
            and must have 5 charecters''', extra_tags='signpass')
            return redirect(user_signup)

    return render(request, 'user/user_signup.html')


def user_login(request):
    if 'user_id' in request.session:
        return redirect(shop)

    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']

        if email == '':
            messages.error(request, 'please enter email')
            return redirect(user_login)
        elif password == '':
            messages.error(request, 'please enter password')
            return redirect(user_login)
        elif Accounts.objects.filter(email=email):
            user = authenticate(request, username=email, password=password)

            if user is not None and user.is_active:
                request.session['user_id'] = email

                login(request, user)
                return redirect(shop)
            else:
                messages.error(request, 'There is No such user')
                return redirect(user_login)
        else:
            messages.error(request, 'Invalid Credentials')
            return redirect(user_login)

    return render(request, 'user/user_login.html')


# @login_required(redirect_field_name="user_login")
def user_logout(request):
    #
    request.session.flush()
    logout(request)
    return redirect(user_login)


# else:
#     return redirect(user_login)


# =======OTP LOGIN====================
import random
from .twilio import MessageHandler


def otp_login(request):
    if request.method == 'POST':
        phone = request.POST['phone_number']

        if not phone or len(phone) != 10:
            messages.error(request, 'in valid Credentials')
        else:
            account_obj = Accounts.objects.get(phone=phone)
            global account_

            def account_():
                return phone

            if account_obj:
                otp = random.randint(1000, 9999)

                message_handler = MessageHandler(('+91' + phone), otp).send_otp_on_phone()
                global otp_id

                def otp_id():
                    return otp

                return redirect(otp_confirm)

    return render(request, 'user/otp_login.html')


def otp_confirm(request):
    if request.method == "POST":
        otp_number = request.POST['otp']

        if int(otp_number) == int(otp_id()):

            phone = account_()
            user = Accounts.objects.filter(phone=phone)
            email = user[0].email
            request.session['user_id'] = email
            return redirect(shop)
            # print(email)

            # password = user[0].password
            # print(password)
            # user = authenticate(request, username=email, password=password)
            # print(user)

        else:
            messages.error(request, 'Otp invalid')

            return redirect(otp_confirm)
    return render(request, 'user/otp.html')


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def shop(request):
    if 'user_id' in request.session:

        search_icon = True

        category = Category.objects.all()
        products = Product.objects.all()

        customer_obj = Accounts.objects.get(email=request.session['user_id'])
        customer = customer_obj.id
        cat = Category.objects.all()
        log = False
        return render(request, 'user/index.html',
                      {'log': log, 'products': products, "cat": cat, 'category': category, 'customer': customer,
                       'search_icon': search_icon}, )
    else:
        search_icon = True
        category = Category.objects.all()
        products = Product.objects.all()

        cat = Category.objects.all()
        log = True

        return render(request, 'user/index.html', {'products': products, "cat": cat, 'category': category, 'log': log,
                                                  'search_icon': search_icon}, )


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def search_results(request):
    if 'user_id' in request.session:
        search = request.GET['search_text']

        products = Product.objects.filter(name__icontains=search)

        search_icon = True

        customer_obj = Accounts.objects.get(email=request.session['user_id'])
        customer = customer_obj.id
        cat = Category.objects.all()
        log = False
        return render(request, 'user/search_results.html',
                      {'log': log, 'products': products, "cat": cat, 'customer': customer, 'search_icon': search_icon,
                       'search_key': search}, )
    else:
        search = request.GET['search_text']
        search_icon = True
        category = Category.objects.all()
        products = Product.objects.filter(name__icontains=search)

        cat = Category.objects.all()
        log = True

        return render(request, 'user/search_results.html',
                      {'products': products, "cat": cat, 'category': category, 'log': log, 'search_icon': search_icon,
                       'search_key': search}, )

    # =====================================================================================


# single product view

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def product_view(request, id):
    # print(e)
    if 'user_id' in request.session:
        product = Product.objects.get(id=id)
        # quantity = product.total_quantity
        customer_obj = Accounts.objects.get(email=request.session['user_id'])
        customer = customer_obj.id
        print(product.total_quantity)
        log = False
        # print(customer)
        return render(request, 'user/product_view.html', {'log': log, 'item': product, 'customer': customer})
    else:
        product = Product.objects.get(id=id)
        # quantity = product.total_quantity

        print(product.total_quantity)
        log = True
        # print(customer)
        return render(request, 'user/product_view.html', {'item': product, 'log': log})


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def category_list(request, id):
    if 'user_id' in request.session:
        category = Category.objects.all()
        cat = Category.objects.get(id=id)
        products = Product.objects.filter(category_id=id)
        print(products)
        log = False
        return render(request, 'user/category_view.html',
                      {'products': products, 'category': category, 'log': log, 'cat': cat})
    else:
        category = Category.objects.all()

        products = Product.objects.filter(category_id=id)
        print(products)
        log = True
        return render(request, 'user/category_view.html',
                      {'cat': cat, 'products': products, 'category': category, 'log': log})

    # ==============================================================================================
    # Cart management


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def cartview(request):
    if "user_id" in request.session:
        category = Category.objects.all()
        prolist = []
        customer = Accounts.objects.get(email=request.session['user_id'])
        cart = Cart.objects.filter(customer=customer).order_by('created_at')
        try:
            address = Address.objects.get(default_address=True, user=customer)
        except:
            address = None

        cartloop = Cart.objects.filter(customer=customer).values()
        category = Category.objects.all()

        total_sum = 0
        sum = 0

        for i in cartloop:

            product_id = i['product_id']
            quantity = i['quantity']
            product_obj = Product.objects.get(id=product_id)

            if product_obj.total_quantity < quantity:

                prolist.append(product_obj)
                prolistlen = len(prolist)
            else:
                prolist = []
                prolistlen = len(prolist)

            total_sum = total_sum + (product_obj.final_price) * quantity

        total = int(total_sum)
        print(prolist)
        try:

            coupon_avilable = Coupen.objects.get(id=cart[0].coupon_id)
        except:
            coupon_avilable = None

        if coupon_avilable:
            offer_with_coupon = total - coupon_avilable.discount_price
        else:
            offer_with_coupon = None

        log = False
        if cart:
            return render(request, 'user/cartview.html',
                          {'category': category, 'prolistlen': prolistlen, 'prolist': prolist, 'log': log, 'cart': cart,
                           'total': total, 'category': category, 'coupon_avilable': coupon_avilable,
                           'offer_with_coupon': offer_with_coupon, 'address': address})
        else:
            return render(request, 'user/cartview.html', {'category': category})
    else:

        log = True
        try:
            cart = request.session['cartdata']
        except:
            cart = None
        total_amt = 0
        if 'cartdata' in request.session:
            for p_id, item in request.session['cartdata'].items():
                total_amt += int(item['qty']) * int(item['price'])

            return render(request, 'user/cartview_guest.html',
                          {'log': log, 'data': request.session['cartdata'], 'cart_data': request.session['cartdata'],
                           'totalitems': len(request.session['cartdata']), 'total_amt': total_amt})
        else:
            return render(request, 'user/cartview_guest.html',
                          {'log': log, 'cart_data': '', 'totalitems': 0, 'total_amt': total_amt})


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def add_cart(request, id):
    if "user_id" in request.session:

        product_id = id

        customer_obj = Accounts.objects.get(email=request.session['user_id'])
        customer_id = customer_obj.id
        obj = Cart.objects.filter(product_id=product_id, customer_id=customer_id)

        if obj:
            product_query_obj = obj[0]
            current_quantity = product_query_obj.quantity
            print(current_quantity)
            total_quantity = product_query_obj.product.total_quantity
            print(product_query_obj.product.total_quantity)

            if total_quantity > 0 and total_quantity > current_quantity:
                current_quantity = current_quantity + 1
                cart = Cart.objects.get(product_id=product_id, customer_id=customer_id)
                cart.quantity = current_quantity
                cart.save()
            return HttpResponse('')
        else:

            cart = Cart.objects.create(product_id=product_id, customer_id=customer_id)
            cart.save()
            return HttpResponse('')

    else:
        product = Product.objects.get(id=id)
        cart_p = {}
        cart_p[str(id)] = {
            'image': str(product.image),
            'name': product.name,
            'price': product.price,
            'qty': int(1), }
        if 'cartdata' in request.session:
            if str(id) in request.session['cartdata']:
                cart_data = request.session['cartdata']
                cart_data[str(id)]['qty'] = int(cart_p[str(id)]['qty'])
                cart_data.update(cart_data)
                request.session['cartdata'] = cart_data
            else:
                cart_data = request.session['cartdata']
                cart_data.update(cart_p)
                request.session['cartdata'] = cart_data
        else:
            request.session['cartdata'] = cart_p

        print(cart_p)
        return JsonResponse({'data': request.session['cartdata'], 'totalitems': len(request.session['cartdata'])})


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def add_cart_product_view(request, id):
    if "user_id" in request.session:
        product_id = id

        customer_obj = Accounts.objects.get(email=request.session['user_id'])
        customer_id = customer_obj.id
        obj = Cart.objects.filter(product_id=product_id, customer_id=customer_id)

        if obj:
            product_query_obj = obj[0]
            current_quantity = product_query_obj.quantity
            current_quantity = current_quantity + 1
            cart = Cart.objects.get(product_id=product_id, customer_id=customer_id)
            cart.quantity = current_quantity
            cart.save()
            return HttpResponse('')
        else:
            cart = Cart.objects.create(product_id=product_id, customer_id=customer_id)
            cart.save()
            return HttpResponse('')


    else:
        return redirect(user_login)


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def delete_cart(request):
    if "user_id" in request.session:
        customer_obj = Accounts.objects.get(email=request.session['user_id'])
        cart = Cart.objects.filter(customer=customer_obj)

        cart.delete()
        return redirect(cartview)
    else:
        del request.session['cartdata']
        return redirect(cartview)


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def delete_product_cart(request, id):
    if "user_id" in request.session:
        cart = Cart.objects.get(id=id)
        print(id)
        cart.delete()

        return redirect(cartview)
    else:
        id = str(11)
        print('hellooodadadadddddd')
        del request.session['cartdata'][id]
        print('riyaaahhhhhhhhhh')
        return redirect(cartview)


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def plus_cart_quantity(request, quantity, id):
    cart_obj = Cart.objects.filter(id=id, )
    product_query_obj = cart_obj[0]
    product = product_query_obj.product
    current_quantity = product_query_obj.quantity
    product_id = product.id

    if product.total_quantity > 0 and current_quantity < product.total_quantity:

        print(product_query_obj)
        current_quantity = product_query_obj.quantity
        current_quantity = current_quantity + 1
        print(current_quantity)
        cart_obj.quantity = current_quantity
        Cart.objects.filter(id=id).update(quantity=current_quantity)

        return HttpResponse('success')


    else:

        return HttpResponse('success')


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def minus_cart_quantity(request, quantity, id):
    cart_obj = Cart.objects.filter(id=id, )
    product_query_obj = cart_obj[0]
    current_quantity = product_query_obj.quantity
    product = product_query_obj.product
    product_id = product.id

    if current_quantity > 1:

        # ========= cart stock increment==============

        cart_obj = Cart.objects.filter(id=id, )
        product_query_obj = cart_obj[0]
        print(product_query_obj)
        current_quantity = product_query_obj.quantity
        current_quantity = current_quantity - 1
        print(current_quantity)
        cart_obj.quantity = current_quantity
        Cart.objects.filter(id=id).update(quantity=current_quantity)

        return HttpResponse('success')

    else:
        return HttpResponse('success')


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def update_quantity(request, id):
    quantity = id
    return HttpResponse('success')

    # ====================ORDER MANAGEMENT =======================================================


# CHECKOUT PAGE

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def choose_address_select(request):
    if "user_id" in request.session:
        user = Accounts.objects.get(email=request.session['user_id'])

        try:
            address = Address.objects.filter(user_id=user.id)
            address_query = address[0]
            #   try:
            #     def_address = Address.objects.get(default_address = True, user=user
            #                                     )
            #   except:
            #        def_address = Address.objects.get(default_address = True, user=user
            #                                     )
            print(address_query.id)
            # return address
        except:
            print('please add an address')
            address = None

        # print(user)
        return render(request, 'user/checkout.html', {'address': address})
    else:
        return redirect(user_login)

    # +++++++ORDER MANAGEMENT+++++++++++++++++++


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def choose_address(request):
    if "user_id" in request.session:
        if request.method == 'POST':
            address_id = request.POST['address']
            global check_out_address

            def check_out_address():
                return address_id

            Address.objects.all().update(default_address=False)
            address = Address.objects.get(id=address_id)
            address.default_address = True
            address.save()

            print(address_id)
            return redirect(cartview)
    else:
        return redirect(user_login)


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def choose_payment_method(request, id):
    if "user_id" in request.session:
        customer = Accounts.objects.get(email=request.session['user_id'])
        cart = Cart.objects.filter(customer=customer).order_by('created_at')
        cartloop = Cart.objects.filter(customer=customer).values()

        total_sum = 0
        prolist = []
        for i in cartloop:

            # ===========================================================
            product_id = i['product_id']
            quantity = i['quantity']
            product_obj = Product.objects.get(id=product_id)

            if product_obj.total_quantity < quantity:

                prolist.append(product_obj)
                prolistlen = len(prolist)
            else:
                prolist = []
                prolistlen = len(prolist)

            print(product_obj.final_price)

            total_sum = total_sum + (product_obj.final_price) * quantity

        print(total_sum)
        total = total_sum
        # ============================================================

        address = Address.objects.filter(id=id)

        cart = Cart.objects.filter(customer=customer).order_by('created_at')

        try:

            coupon_avilable = Coupen.objects.get(id=cart[0].coupon_id)
        except:
            coupon_avilable = None

        if coupon_avilable:
            offer_with_coupon = total - coupon_avilable.discount_price
        else:
            offer_with_coupon = total

        return render(request, 'user/payment_method.html',
                      {'prolistlen': prolistlen, 'prolist': prolist, 'address': address, 'address_id': id,
                       'cart_total': total, 'coupon_avilable': coupon_avilable,
                       'offer_with_coupon': offer_with_coupon}, )
    else:
        return redirect(user_login)


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def update_address(request, id):
    if "user_id" in request.session:
        # form = CustomerForm()
        # context = {'form':form}
        print(messages)
        if request.method == 'POST':
            user = Accounts.objects.get(email=request.session['user_id'])
            name = request.POST['name']
            phone = request.POST['phone']
            house_name = request.POST['house_name']
            street_name = request.POST['street_name']
            landmark = request.POST['landmark']
            city = request.POST['city']
            pin = request.POST['pin']

            if len(phone) != 10:
                messages.error(request, 'Cedentials invalid')


            elif len(pin) != 6:
                messages.error(request, 'Cedentials invalid')
            else:

                Address.objects.filter(id=id).update(user=user, name=name, phone_number=phone, house_name=house_name,
                                                     street_name=street_name, landmark=landmark, city=city,
                                                     pin_code=pin)
                messages.success(request, 'Address Updated successfully')
    address = Address.objects.get(id=id)

    return render(request, 'user/update_address.html', {'item': address, 'address_id': id})


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def update_address_user(request, id):
    if "user_id" in request.session:
        # form = CustomerForm()
        # context = {'form':form}
        print(messages)
        if request.method == 'POST':
            user = Accounts.objects.get(email=request.session['user_id'])
            name = request.POST['name']
            phone = request.POST['phone']
            house_name = request.POST['house_name']
            street_name = request.POST['street_name']
            landmark = request.POST['landmark']
            city = request.POST['city']
            pin = request.POST['pin']

            if len(phone) != 10:
                messages.error(request, 'Cedentials invalid')


            elif len(pin) != 6:
                messages.error(request, 'Cedentials invalid')
            else:

                Address.objects.filter(id=id).update(user=user, name=name, phone_number=phone, house_name=house_name,
                                                     street_name=street_name, landmark=landmark, city=city,
                                                     pin_code=pin)
                messages.success(request, 'Address Updated successfully')
    address = Address.objects.get(id=id)

    return render(request, 'user/update_address_user.html', {'item': address, 'address_id': id})

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def delete_address_user(request, id):
    if "user_id" in request.session:
        user = Address.objects.get(id=id)
        user.delete()
        return redirect(userprofile)
    else:
        return redirect(user_login)

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def choose_payment(request):
    if "user_id" in request.session:

        if request.method == 'GET':
            payment_method = request.GET['optradio']
            amount = request.GET['cart_total']
            if payment_method == 'RAZORPAY':
                return redirect('razorpay_pay', amount)
            elif payment_method == 'COD':
                return redirect('create_order', 1)
            elif payment_method == 'PAYPAL':
                return redirect('paypal', amount)
            else:
                return redirect(shop)


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def create_order(request, id):
    if "user_id" in request.session:

        print(type(id), id)
        if id == 1:
            payment_method = 'COD'
            is_paid = False
        elif id == 3:
            payment_method = 'PAYPAL'
            is_paid = True
        elif id == 2:
            payment_method = 'RAZORPAY'
            is_paid = True
        customer = Accounts.objects.get(email=request.session['user_id'])
        address = Address.objects.get(default_address=True, user=customer)
        cart = Cart.objects.filter(customer=customer).order_by('created_at')

        cartloop = Cart.objects.filter(customer=customer).values()

        total_sum = 0
        for i in cartloop:
            # ===========================================================
            product_id = i['product_id']
            quantity = i['quantity']
            product_obj = Product.objects.get(id=product_id)

            print(product_obj.final_price)

            total_sum = total_sum + (product_obj.final_price) * quantity

        amount = total_sum

        name = address.name
        phone_number = address.phone_number
        house_name = address.house_name
        street_name = address.street_name
        landamrk = address.landmark
        city = address.city
        pincode = address.pin_code

        tracking_no = str(customer) + str(random.randint(1111111, 9999999))
        while OrderTable.objects.filter(tracking_no=tracking_no) is None:
            tracking_no = customer + str(random.randint(1111111, 9999999))
        tracking_no = tracking_no

        try:

            coupon_avilable = Coupen.objects.get(id=cart[0].coupon_id)
        except:
            coupon_avilable = None

        if coupon_avilable:
            amount = int(amount) - int(coupon_avilable.discount_price)
            order = OrderTable.objects.create(user=customer, amount=amount, payment_method=payment_method,
                                              name=name, phone_number=phone_number, house_name=house_name,
                                              street_name=street_name, landamrk=landamrk, city=city, pincode=pincode,

                                              tracking_no=tracking_no, coupon=coupon_avilable, is_paid=is_paid)

        else:
            order = OrderTable.objects.create(user=customer, amount=amount, payment_method=payment_method,
                                              name=name, phone_number=phone_number, house_name=house_name,
                                              street_name=street_name, landamrk=landamrk, city=city, pincode=pincode,

                                              tracking_no=tracking_no, is_paid=is_paid)

        ordr_query = OrderTable.objects.get(tracking_no=tracking_no)
        print(ordr_query)

        for cart in cart:
            item_quantity = cart.quantity
            product = Product.objects.get(id=cart.product_id)
            print(item_quantity, product)
            OrderItem.objects.create(order=ordr_query, product_name=product.name, product=product, price=product.price,
                                     quantity=item_quantity)
            item_quantity = product.total_quantity - item_quantity
            Product.objects.filter(id=cart.product_id).update(total_quantity=item_quantity)
            if item_quantity < 1:
                Product.objects.filter(id=cart.product_id).update(instock=False)
            elif item_quantity >= 1:
                Product.objects.filter(id=cart.product_id).update(instock=True)
            cart.delete()

        return redirect(payment_success_page)
    else:
        return redirect(user_login)


# ===========PAYMENT METHODS====================
from VEGIE_PROJECT.settings import razor_pay_api_key, razor_pay_secret_key

import razorpay

client = razorpay.Client(auth=(razor_pay_api_key, razor_pay_secret_key))


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def razorpay_pay(request, amount):
    if "user_id" in request.session:

        # print(order_id())
        # order = OrderTable.objects.get(id=id)
        # OrderTable.objects.filter(id=id).update(is_paid=True)

        user = Accounts.objects.get(email=request.session['user_id'])
        cart = Cart.objects.filter(customer=user).order_by('created_at')
        try:

            coupon_avilable = Coupen.objects.get(id=cart[0].coupon_id)
        except:
            coupon_avilable = None

        if coupon_avilable:
            amount = int(amount) - int(coupon_avilable.discount_price)
        else:
            amount = amount
        print(amount)
        # print(type(order.amount))
        import razorpay

        DATA = {
            "amount": (amount) * 100,
            "currency": "INR",
            'payment_capture': '1',
            # "receipt": "receipt#1",
            # "notes": {
            #     "key1": "value3",
            #     "key2": "value2"
            # }
        }
        razor_order = client.order.create(data=DATA)
        razor_id = razor_order['id']

        return render(request, 'user/razorpay.html', {'order_id': razor_id, "order_amount": amount, 'user': user})
    else:
        return redirect(user_login)


@csrf_exempt
def razorpay_success(request):
    if "user_id" in request.session:
        return redirect('create_order', 2)
    else:
        return redirect(user_login)


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def paypal(request, amount):
    if "user_id" in request.session:

        user = Accounts.objects.get(email=request.session['user_id'])

        cart = Cart.objects.filter(customer=user).order_by('created_at')
        try:

            coupon_avilable = Coupen.objects.get(id=cart[0].coupon_id)
        except:
            coupon_avilable = None

        if coupon_avilable:
            amount = int(amount) - int(coupon_avilable.discount_price)
        else:
            amount = amount
        # print(amount)
        # print(type(amount))     
        return render(request, 'user/paypal.html', {"order_amount": amount, 'user': user})
    else:
        return redirect(user_login)


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def paypalsuccess(request):
    if "user_id" in request.session:
        return redirect('create_order', 3)
    else:
        return redirect(user_login)


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def cod_success(request):
    if "user_id" in request.session:
        return redirect('create_order', 1)
    else:
        return redirect(user_login)


@csrf_exempt
def payment_success(request):
    if "user_id" in request.session:
        return redirect('create_order', 2)
    else:
        return redirect(user_login)


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def payment_success_page(request):
    if "user_id" in request.session:
        return render(request, 'user/payment_success.html')
    else:
        return redirect(user_login)


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def payment_failed(request):
    if "user_id" in request.session:
        return render(request, 'user/payment_failed.html')
    else:
        return redirect(user_login)


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def order_user(request):
    category = Category.objects.all()
    if "user_id" in request.session:
        order = OrderTable.objects.all().order_by('created_at').values()

        p = Paginator(order, 10)
        page_num = request.GET.get('page', 1)

        try:

            page = p.page(page_num)
        except EmptyPage:
            page = p.page(1)

        return render(request, 'user/order_user.html', {'order': order, 'category': category}, )
    else:
        return redirect(user_login)


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def active_orders(request):
    category = Category.objects.all()
    if "user_id" in request.session:
        order = OrderTable.objects.filter(Q(status='Confirmed') | Q(status='Pending')).order_by('created_at').values()
        products = OrderItem.objects.all()
        p = Paginator(order, 10)
        page_num = request.GET.get('page', 1)

        try:

            page = p.page(page_num)
        except EmptyPage:
            page = p.page(1)

        return render(request, 'user/active_orders.html', {'order': order, 'category': category}, )
    else:
        return redirect(user_login)


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def active_order_products(request, id):
    if "user_id" in request.session:
        # order    = OrderTable.objects.filter(status='Confirmed').order_by('created_at').values()
        products = OrderItem.objects.filter(order_id=id)

        for item in products:
            product = Product.objects.get(id=item.product_id)
            quantity = item.quantity
            print(product, quantity)
            # print(product.id)
            # product.total_quantity=product.total_quantity+quantity
            # product.save()
            # Product.objects.filter(id=product.id).update()

        print(products)

        return render(request, 'user/active_order_products.html', {'products': products}, )
    else:
        return redirect(user_login)


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def delivered_orders(request):
    if "user_id" in request.session:
        category = Category.objects.all()
        order = OrderTable.objects.filter(status='Delivered')

        p = Paginator(order, 10)
        page_num = request.GET.get('page', 1)

        try:

            page = p.page(page_num)
        except EmptyPage:
            page = p.page(1)

        return render(request, 'user/delivered_orders.html', {'order': order, 'category': category})
    else:
        return redirect(user_login)

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def return_order(request, id):
    if "user_id" in request.session:
        pass

        order_products = OrderItem.objects.filter(order_id=id)
        order = OrderTable.objects.get(id=id)
        order.status = "Returned"
        order.save()

        try:
            Wallet.objects.get(user=Accounts.objects.get(email=request.session['user_id']))
            wallet = Wallet.objects.get(user=Accounts.objects.get(email=request.session['user_id']))

            wallet.Balance += order.amount
            wallet.save()
        except:
            wallet = Wallet.objects.create(user=Accounts.objects.get(email=request.session['user_id']),
                                           Balance=order.amount)

        for item in order_products:
            product = Product.objects.get(id=item.product_id)
            quantity = item.quantity
            print(product, quantity)
            product.total_quantity = product.total_quantity + quantity
            product.save()
        WalletTransactions.objects.create(amount=order.amount,
                                          user=Accounts.objects.get(email=request.session['user_id']), status='CREDIT')
        print(order.amount)

        print(order.amount)

        return redirect(delivered_orders)
        # return HttpResponse('ghghhghg')
    else:
        return redirect(user_login)


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def order_cancel_user(request, id):
    if "user_id" in request.session:

        OrderTable.objects.filter(id=id).update(status='Canceled')

        order_products = OrderItem.objects.filter(order_id=id)
        for item in order_products:
            product = Product.objects.get(id=item.product_id)
            quantity = item.quantity
            print(product, quantity)

            if product.total_quantity == 0:

                product.total_quantity = product.total_quantity + quantity
                product.instock = True
                product.save()

            else:

                product.total_quantity = product.total_quantity + quantity

        return redirect(active_orders)

    else:
        return redirect(user_login)


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def view_order_user(request, id):
    category = Category.objects.all()
    if "user_id" in request.session:

        order = OrderTable.objects.get(id=id)

        products = OrderItem.objects.filter(order_id=id)
        try:
            coupon = Coupen.objects.get(id=order.coupon_id)
        except:
            coupon = None

        return render(request, 'user/vieworderuser.html',
                      {'order': order, 'category': category, 'products': products, 'coupon': coupon})

    else:
        return redirect(user_login)

    # =======User profile======================================


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def userprofile(request):
    category = Category.objects.all()
    if "user_id" in request.session:
        user = Accounts.objects.get(email=request.session['user_id'])
        address = Address.objects.filter(user_id=user.id)
        try:
            wallet = Wallet.objects.get(user=user)
        except:
            wallet = None
        print(user)

        return render(request, 'user/userprofile.html',
                      {'user': user, 'category': category, 'address': address, 'wallet': wallet})
    else:
        return redirect(user_login)


from .forms import CustomerForm


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def add_address(request):
    if "user_id" in request.session:
        # form = CustomerForm()
        # context = {'form':form}
        print(messages)
        if request.method == 'POST':
            user = Accounts.objects.get(email=request.session['user_id'])
            name = request.POST['name']
            phone = request.POST['phone']
            house_name = request.POST['house_name']
            street_name = request.POST['street_name']
            landmark = request.POST['landmark']
            city = request.POST['city']
            pin = request.POST['pin']

            phone_number_obj = Address.objects.filter(phone_number=phone)
            if phone_number_obj:
                print('phoneobj')
                messages.error(request, 'Phone number is already registered')
            elif len(phone) != 10:
                messages.error(request, 'Credentials invalid')
                print('phonelen')

            elif len(pin) != 6:
                messages.error(request, 'Credentials invalid')
                print('pin')
            else:

                Address.objects.create(user=user, name=name, phone_number=phone, house_name=house_name,
                                       street_name=street_name, landmark=landmark, city=city, pin_code=pin)
                messages.success(request, 'Address added successfully')

    return render(request, 'user/add_address.html')


def coupon(request, subtotal):
    return redirect(cartview)

def apply_coupon(request, id):
    from adminapp.models import user_coupon

    if "user_id" in request.session:

        coupon_code = request.GET['coupon_code']
        try:
            coupon = Coupen.objects.get(coupen_code=str(coupon_code))
        except:
            coupon = None
        customer = Accounts.objects.get(email=request.session['user_id'])
        cart = Cart.objects.filter(customer=customer)
        cartloop = Cart.objects.filter(customer=customer).values()
        cu = Coupen.objects.all()
        try:
            user_coupon_obj = user_coupon.objects.get(coupon=coupon, user=customer)
        except:
            user_coupon_obj = None
        total_sum = 0
        for i in cartloop:
            # ===========================================================
            product_id = i['product_id']
            quantity = i['quantity']
            product_obj = Product.objects.get(id=product_id)

            # print(product_obj.final_price)

            total_sum = total_sum + (product_obj.final_price) * quantity
        total = total_sum
        # ===
        if coupon:

            if int(total) >= coupon.minimum_amount:

                if cart[0].coupon == None and user_coupon_obj is None:
                    user_coupon.objects.create(coupon=coupon, user=customer)
                    Cart.objects.filter(customer=customer).update(coupon=coupon)
                    messages.info(request, "Coupon applied successfully !")

                else:
                    messages.info(request, 'Coupon already applied ! ')

            else:
                messages.info(request, f'Aleast spent Rs {coupon.minimum_amount} ! ')

            return redirect('choose_payment_method', id)
        elif coupon_code == '':
            messages.error(request, 'Please enter a coupon code ! ')
            return redirect('choose_payment_method', id)
        else:
            messages.error(request, 'Not a valid coupon !')
            return redirect('choose_payment_method', id)

    else:
        return redirect('choose_payment_method', id)


def guest_user(request):
    return render(request, 'guest_user.html', )


def wallet(request):
    if "user_id" in request.session:

        user = Accounts.objects.get(email=request.session['user_id'])

        try:
            wallet = Wallet.objects.get(user=user)
        except:
            wallet = None
        print(user)
        wallet_transactions = WalletTransactions.objects.filter(user=user)
        return render(request, 'user/wallet.html', {'wallet': wallet, 'wallet_transactions': wallet_transactions})
    else:
        return redirect('choose_payment_method', id)


def test(request):
    return render(request, 'test.html')

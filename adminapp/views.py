import imp
from math import prod
from unicodedata import name
from urllib import response
from django.shortcuts import render, redirect
from accounts.models import Accounts
from django.contrib.auth import authenticate
from django.contrib.auth import logout, login
from django.contrib import messages
from .models import Product, Category
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_control
from userapp.models import OrderItem, OrderTable
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage
import datetime
import json

from datetime import timedelta
from django.utils import timezone

# csv and pdf
from django.http import JsonResponse, FileResponse
import io
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter

import xlwt

from django.http import FileResponse, HttpResponse
import io
import csv


# Create your views here.

# admin login
def admin_login(request):
    if 'admin_id' in request.session:
        return redirect(admin_home)
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('pass1')
        if email == '' and password == '':
            messages.error(request, 'Please enter Email and password !')
            return redirect(admin_login)

        elif email != 'admin@veggie.com':
            messages.error(request, 'Only admin can Login!!!')
            return redirect(admin_login)

        elif Accounts.objects.filter(email=email):
            admin = authenticate(request, username=email, password=password)
            if admin is not None:
                request.session['admin_id'] = email
                login(request, admin)
                return redirect(admin_home)
            else:
                messages.error(request, 'Invalid credentials')
                return redirect(admin_login)
        else:
            messages.error(request, 'Invalid credentials')
            return redirect(admin_login)
    return render(request, 'admin/admin_login.html')


def admin_logout(request):
    if 'admin_id' in request.session:
        request.session.flush()
        logout(request)
        return redirect(admin_login)
    else:
        return redirect(admin_login)


# ===============================================================================================================================

# Admin    Customers    Products    
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def admin_home(request):
    if 'admin_id' in request.session:
        products = Product.objects.all()
        confirmed_orders = OrderTable.objects.filter(status='Confirmed').count()
        pending_orders = OrderTable.objects.filter(status='Pending').count()
        delivered_orders = OrderTable.objects.filter(status='Delivered').count()
        from datetime import timedelta
        from django.utils import timezone

        order_today = OrderTable.objects.filter(date_delivered=datetime.date.today(), status='Delivered').count()
        order_today_obj = OrderTable.objects.filter(date_delivered=datetime.date.today(), status='Delivered')
        revenue_today = 0
        for i in order_today_obj:
            revenue_today = i.amount + revenue_today
        some_day_last_week = datetime.date.today() - datetime.timedelta(days=7)

        order_lastweek = OrderTable.objects.filter(date_delivered__gte=some_day_last_week,
                                                   date_delivered__lte=datetime.date.today(),
                                                   status='Delivered').count()
        order_lastweek_obj = OrderTable.objects.filter(date_delivered__gte=some_day_last_week,
                                                       date_delivered__lte=datetime.date.today(), status='Delivered')
        revenue_lastweek = 0
        for i in order_lastweek_obj:
            revenue_lastweek = i.amount + revenue_lastweek

        some_day_last_year = datetime.date.today() - datetime.timedelta(days=365)

        order_lastyear = OrderTable.objects.filter(date_delivered__gte=some_day_last_year,
                                                   date_delivered__lte=datetime.date.today(),
                                                   status='Delivered').count()
        order_lastyear_obj = OrderTable.objects.filter(date_delivered__gte=some_day_last_year,
                                                       date_delivered__lte=datetime.date.today(), status='Delivered')

        revenue_lastyear = 0
        for i in order_lastyear_obj:
            revenue_lastyear = i.amount + revenue_lastyear

        yesterday = datetime.date.today() - datetime.timedelta(days=1)
        yesterday_1 = datetime.date.today() - datetime.timedelta(days=2)
        yesterday_2 = datetime.date.today() - datetime.timedelta(days=3)
        yesterday_3 = datetime.date.today() - datetime.timedelta(days=4)
        yesterday_4 = datetime.date.today() - datetime.timedelta(days=5)
        yesterday_5 = datetime.date.today() - datetime.timedelta(days=6)
        yesterday_6 = datetime.date.today() - datetime.timedelta(days=7)
        print(yesterday)
        order_yesterday = OrderTable.objects.filter(date_delivered__gte=yesterday,
                                                    date_delivered__lte=datetime.date.today(),
                                                    status='Delivered').count()
        order_yesterday_1 = OrderTable.objects.filter(date_delivered__gte=yesterday_1, date_delivered__lte=yesterday,
                                                      status='Delivered').count()
        order_yesterday_2 = OrderTable.objects.filter(date_delivered__gte=yesterday_2, date_delivered__lte=yesterday_1,
                                                      status='Delivered').count()
        order_yesterday_3 = OrderTable.objects.filter(date_delivered__gte=yesterday_3, date_delivered__lte=yesterday_2,
                                                      status='Delivered').count()
        order_yesterday_4 = OrderTable.objects.filter(date_delivered__gte=yesterday_4, date_delivered__lte=yesterday_3,
                                                      status='Delivered').count()
        order_yesterday_5 = OrderTable.objects.filter(date_delivered__gte=yesterday_5, date_delivered__lte=yesterday_4,
                                                      status='Delivered').count()
        order_yesterday_6 = OrderTable.objects.filter(date_delivered__gte=yesterday_6, date_delivered__lte=yesterday_5,
                                                      status='Delivered').count()

        context = {'revenue_today': revenue_today,
                   'revenue_lastweek': revenue_lastweek,
                   'revenue_lastyear': revenue_lastyear,

                   'order_today': order_today,
                   'yesterday': yesterday,
                   'yesterday_1': yesterday_1,
                   'yesterday_2': yesterday_2,
                   'yesterday_3': yesterday_3,
                   'yesterday_4': yesterday_4,
                   'yesterday_5': yesterday_5,
                   'yesterday_6': yesterday_6,

                   'order_yesterday': order_yesterday,
                   'order_yesterday_1': order_yesterday_1,
                   'order_yesterday_2': order_yesterday_2,
                   'order_yesterday_3': order_yesterday_3,
                   'order_yesterday_4': order_yesterday_4,
                   'order_yesterday_5': order_yesterday_5,
                   'order_yesterday_6': order_yesterday_6,

                   'confirmed_orders': confirmed_orders,
                   'pending_orders': pending_orders,
                   'delivered_orders': delivered_orders,

                   'order_today': order_today,
                   'order_lastweek': order_lastweek,
                   'order_lastyear': order_lastyear,

                   }

        print(type(confirmed_orders))

        return render(request, 'admin/admin_home.html', context)
    else:
        return render(request, 'admin/admin_login.html')


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def customers(request):
    if 'admin_id' in request.session:
        customers = Accounts.objects.filter(is_active=True, is_superuser=False).order_by('first_name').values()

        return render(request, 'admin/customers.html', {'customers': customers})
    else:

        return render(request, 'admin/admin_login.html')


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def view_customer(request, id):
    if 'admin_id' in request.session:
        customer = Accounts.objects.get(id=id)

        return render(request, 'admin/view_customer.html', {'customer': customer})
    else:

        return redirect(admin_login())


# ===============================================================================================================================

#  Block    Unblock       
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def block(request, id):
    Accounts.objects.filter(id=id).update(is_active=False)
    print(id)
    messages.success(request, 'User Blocked sucessfully', )
    return redirect('customers')

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def unblock(request, id):
    Accounts.objects.filter(id=id).update(is_active=True)
    messages.success(request, 'User Unblocked sucessfully', )
    return redirect('blocked_customers')


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def blocked_customers(request):
    if 'admin_id' in request.session:
        customers = Accounts.objects.filter(is_active=False, is_superuser=False).order_by('first_name').values()

        return render(request, 'admin/blocked_customers.html', {'customers': customers})
    else:
        return redirect(admin_login)


# Product CRUD ========================================================================================================================


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def products(request):
    if 'admin_id' in request.session:
        products = Product.objects.all().order_by('name').values()

        p = Paginator(products, 7)
        page_num = request.GET.get('page', 4)

        # print("NUMBER OF PAGES")
        # print(p.num_pages)
        try:

            page = p.page(page_num)
        except EmptyPage:
            page = p.page(1)
        # print(page)

        print(products[0])
        for item in products.values():
            print('heyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy')
            print()
            print('grrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrr')
        return render(request, 'admin/products.html', {'products': products, })

    else:
        return redirect(admin_login)


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def view_product(request, id):
    if 'admin_id' in request.session:
        product = Product.objects.get(id=id)

        return render(request, 'admin/view_product.html', {'product': product, })


    else:
        return redirect(admin_login)


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def add_product(request):
    if 'admin_id' in request.session:
        cat = None
        if request.method == 'POST':
            name = request.POST['name']
            description = request.POST['product_description']
            price = request.POST['price']
            total_quantity = request.POST['quantity']

            category = Category.objects.get(id=request.POST['category'])

            # try:
            #     offer = request.POST['offer']
            # except:
            #     offer = 0
            if request.POST['offer']:
                offer = request.POST['offer']
            else:
                offer = 0
            print(offer)
            print(type(offer))
            image = image2 = image3 = ''
            try:
                image = request.FILES['uploadFromPC']
                image2 = request.FILES['uploadFromPC2']
                image3 = request.FILES['uploadFromPC3']
            except:
                print('please add an image')

            if name == '' or description == '' or price == '' or total_quantity == '' or image == '':
                messages.error(request, 'All fields are required')
            elif int(price) < 0:
                messages.error(request, 'Negative number is not supportted for price and stock',
                               extra_tags='productadderror')
                return redirect(add_product)
            elif category == '':
                messages.error(request, 'Please select a category', extra_tags='productadderror')
                return redirect(add_product)
            elif offer == '' or int(offer) < 0 or int(offer) > 100:
                messages.error(request, 'Offer must be between 1 and 100', extra_tags='productadderror')
                return redirect(add_product)

            elif image == None or image2 == None or image3 == None or (image == None and image2 == None) or (
                    (image == None and image3 == None) or (image3 == None and image2 == None) or (
            (image == None and image2 == None and image3 == None))):
                messages.error(request, 'Please add product image', extra_tags='productadderror')
                return redirect(add_product)


            else:
                product = Product.objects.create(name=name, category=category, description=description, price=price,
                                                 total_quantity=total_quantity, image=image, offer=offer, image2=image2,
                                                 image3=image3)
                product.save()
                messages.success(request, 'Product added sucessfully', extra_tags='productadderror')

        cat = Category.objects.all()
        return render(request, 'admin/add_product.html', {'cat': cat})

    else:
        return redirect(admin_login)


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def delete_product(request, id):
    if 'admin_id' in request.session:
        product = Product.objects.get(id=id)
        product.delete()
        return redirect(products)
    else:
        return redirect(admin_login)


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def update_product(request, id):
    if 'admin_id' in request.session:
        cat = None
        product = Product.objects.get(id=id)
        if request.method == 'POST':
            name = request.POST['name']
            description = request.POST['product_description']
            price = request.POST['price']
            total_quantity = int(request.POST['quantity'])
            if request.POST['offer']:
                offer = request.POST['offer']
            else:
                offer = 0
            # image = image2 = image3 =''
            # try:
            #         image = request.FILES['uploadFromPC']
            #         image2 = request.FILES['uploadFromPC2']
            #         image3 = request.FILES['uploadFromPC3']
            # except:
            #         print('please add an image')
            if (total_quantity > 0):
                instock = True

            else:
                instock = False
            try:
                categ = request.POST['category']
            except:
                categ = None

            try:
                image = request.FILES['uploadFromPC']
            except:
                image = None
            try:
                image2 = request.FILES['uploadFromPC2']
            except:
                image2 = None
            try:
                image3 = request.FILES['uploadFromPC3']
            except:
                image3 = None

            if categ:
                category = Category.objects.get(id=request.POST['category'])
            else:
                category = Category.objects.get(id=product.category_id)

            if name == '' or description == '' or price == '' or total_quantity == '':
                messages.error(request, 'All fields are required')
            elif int(price) < 0:
                messages.error(request, 'Negative number is not supportted for price and stock',
                               extra_tags='productadderror')
                return redirect('update_product', id)
            elif offer == '' or int(offer) < 0 or int(offer) > 100:
                messages.error(request, 'Offer must be between 1 and 100', extra_tags='productadderror')
                return redirect('update_product', id)
            elif category == '':
                messages.error(request, 'Please select a category', extra_tags='productadderror')
                return redirect('update_product', id)

            # elif image == None or image2==None or image3 == None or (image == None and image2==None) or ((image == None and image3==None) or (image3 == None and image2==None) or ((image == None and image2==None and image3==None)))  :
            #     messages.error(request,'Please add product image', extra_tags='productadderror')
            #     return redirect('update_product', id)
            if image:

                product = Product.objects.get(id=id)
                product.name = name
                product.category = category
                product.description = description
                product.price = price
                product.total_quantity = total_quantity
                product.image = image

                product.instock = instock
                product.save()
                messages.success(request, 'Product updated sucessfully', extra_tags='productadderror')
            elif image2:

                product = Product.objects.get(id=id)
                product.name = name
                product.category = category
                product.description = description
                product.price = price
                product.total_quantity = total_quantity
                product.image2 = image2

                product.instock = instock
                product.save()
                messages.success(request, 'Product updated sucessfully', extra_tags='productadderror')
            elif image3:

                product = Product.objects.get(id=id)
                product.name = name
                product.category = category
                product.description = description
                product.price = price
                product.total_quantity = total_quantity
                product.image3 = image3

                product.instock = instock
                product.save()
                messages.success(request, 'Product updated sucessfully', extra_tags='productadderror')
            elif image and image2:

                product = Product.objects.get(id=id)
                product.name = name
                product.category = category
                product.description = description
                product.price = price
                product.total_quantity = total_quantity
                product.image = image
                product.image2 = image2

                product.instock = instock
                product.save()
                messages.success(request, 'Product updated sucessfully', extra_tags='productadderror')
            elif image and image3:

                product = Product.objects.get(id=id)
                product.name = name
                product.category = category
                product.description = description
                product.price = price
                product.total_quantity = total_quantity
                product.image = image
                product.image3 = image3

                product.instock = instock
                product.save()
                messages.success(request, 'Product updated sucessfully', extra_tags='productadderror')
            elif image2 and image3:

                product = Product.objects.get(id=id)
                product.name = name
                product.category = category
                product.description = description
                product.price = price
                product.total_quantity = total_quantity
                product.image3 = image3
                product.image2 = image2

                product.instock = instock
                product.save()
                messages.success(request, 'Product updated sucessfully', extra_tags='productadderror')
            elif image and image2 and image3:
                image = request.FILES['uploadFromPC']
                image3 = request.FILES['uploadFromPC3']
                image2 = request.FILES['uploadFromPC2']
                product = Product.objects.get(id=id)
                product.name = name
                product.category = category
                product.description = description
                product.price = price
                product.total_quantity = total_quantity
                product.image = image
                product.image3 = image3
                product.image2 = image2

                product.instock = instock
                product.save()
                messages.success(request, 'Product updated sucessfully', extra_tags='productadderror')

            else:
                product = Product.objects.get(id=id)
                product.name = name
                product.category = category
                product.description = description
                product.price = price
                product.total_quantity = total_quantity
                product.offer = offer

                product.instock = instock
                product.save()
                messages.success(request, 'Product updated sucessfully', extra_tags='productadderror')
            # else:
            #     product = Product.objects.get(id=id)
            #     product.name=name
            #     product.category=category
            #     product.description=description
            #     product.price=price
            #     product.total_quantity=total_quantity
            #     product.image=image
            #     product.image2=image2
            #     product.image3=image3
            #     product.instock = instock
            #     product.save()
            #     messages.success(request,'Product updated sucessfully', extra_tags='productadderror')

        cat = Category.objects.all()
        return render(request, 'admin/update_product.html', {'cat': cat, 'product': product}, )

    else:
        return redirect(admin_login)

    # category management ==================================================================================================================


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def categories(request):
    if 'admin_id' in request.session:
        category = Category.objects.all()

        p = Paginator(category, 7)
        page_num = request.GET.get('page', 4)

        # print("NUMBER OF PAGES")
        # print(p.num_pages)
        try:

            page = p.page(page_num)
        except EmptyPage:
            page = p.page(1)
        # print(page)

        return render(request, 'admin/categories.html', {'category': category})

    else:
        return redirect(admin_login)

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def delete_category(request, id):
    cat = Category.objects.get(id=id)
    cat.delete()
    return redirect(categories)


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def add_category(request):
    if 'admin_id' in request.session:
        if request.method == 'POST':
            name = request.POST['name']
            description = request.POST['description']
            offer = request.POST['offer']
            if name == '' or description == '' or offer == '':
                messages.error(request, 'All fields are necessary')
                return redirect(add_category)
            elif offer == '' or int(offer) < 0 or int(offer) > 100:
                messages.error(request, 'Offer must be between 1 and 100', extra_tags='productadderror')
            else:
                category = Category.objects.create(name=name, description=description, offer=offer)
                category.save()
                messages.success(request, 'category added sucessfully')
        return render(request, 'admin/add_category.html')
    else:
        return redirect(admin_login)


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def edit_category(request, id):
    edit_cat = Category.objects.get(id=id)
    if 'admin_id' in request.session:
        if request.method == 'POST':
            name = request.POST['name']
            description = request.POST['description']
            offer = request.POST['offer']
            if name == '' or description == '':
                messages.error(request, 'All fields are necessary')
                return redirect('edit_category', id)
            elif offer == '' or int(offer) < 0 or int(offer) > 100:
                messages.error(request, 'Offer must be between 1 and 100', extra_tags='productadderror')
                return redirect('edit_category', id)
            else:
                category = Category.objects.filter(id=id).update(name=name, description=description, offer=offer)
                messages.success(request, 'category Update sucessfully')
        return render(request, 'admin/edit_category.html', {'edit_cat': edit_cat})
    else:
        return redirect(admin_login)


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def view_category(request, id):
    if 'admin_id' in request.session:
        category = Category.objects.get(id=id)

        product = Product.objects.filter(category=category)

        return render(request, 'admin/view_category.html', {'product': product, 'category': category})

    else:
        return redirect(admin_login)


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def orders(request):
    if 'admin_id' in request.session:
        order = OrderTable.objects.all().order_by('-id').values()
        p = Paginator(order, 10)
        page_num = request.GET.get('page', 1)

        try:

            page = p.page(page_num)
        except EmptyPage:
            page = p.page(1)
        # print(page)
        return render(request, 'admin/orders.html', {'order': order, 'page_number': p})
    else:
        return redirect(admin_login)

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def order_list(request):
    if 'admin_id' in request.session:
        order = OrderTable.objects.all().values_list('name', flat=True)
        orderlist = list(order)
        return JsonResponse(order, safe=False
                            )
    else:
        return redirect(admin_login)


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def order_view(request):
    if 'admin_id' in request.session:

        order = OrderTable.objects.filter(status="Pending").order_by('-id').values()

        p = Paginator(order, 10)
        page_num = request.GET.get('page', 1)

        # print("NUMBER OF PAGES")
        # print(p.num_pages)
        try:

            page = p.page(page_num)
        except EmptyPage:
            page = p.page(1)
        # print(page)

        return render(request, 'admin/order_view.html', {'order': order})
    else:
        return redirect(admin_login)


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def order_delivery(request):
    if 'admin_id' in request.session:
        order = OrderTable.objects.filter(status="Confirmed").order_by('id').values()

        p = Paginator(order, 10)
        page_num = request.GET.get('page', 1)

        try:

            page = p.page(page_num)
        except EmptyPage:
            page = p.page(1)
        # print(page)

        return render(request, 'admin/order_delivery.html', {'order': order})
    else:
        return redirect(admin_login)


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def order_accept(request, id):
    if 'admin_id' in request.session:
        order = OrderTable.objects.filter(id=id).update(status='Confirmed')

        return redirect(order_view)
    else:
        return redirect(admin_login)


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def order_delivered(request, id):
    if 'admin_id' in request.session:

        order = OrderTable.objects.filter(id=id)
        if order[0].is_paid is False:
            order = OrderTable.objects.filter(id=id).update(status='Delivered', is_paid=True,
                                                            date_delivered=datetime.date.today())
            return redirect(order_delivery)

        else:
            order = OrderTable.objects.filter(id=id).update(status='Delivered', date_delivered=datetime.date.today())

        return redirect(order_delivery)
    else:
        return redirect(admin_login)


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def order_reject(request, id):
    if 'admin_id' in request.session:
        print('reject')
        print(id)
        print('halloween')
        order = OrderTable.objects.filter(id=id).update(status='Rejected')

        order_products = OrderItem.objects.filter(order_id=id)
        for item in order_products:
            product = Product.objects.get(id=item.product_id)
            quantity = item.quantity
            print(product, quantity)
            product.total_quantity = product.total_quantity + quantity
            product.save()
        return redirect(order_view)
    else:
        return redirect(admin_login)


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def view_order_admin(request, id):
    if 'admin_id' in request.session:

        order = OrderTable.objects.get(id=id)

        products = OrderItem.objects.filter(order_id=id)
        try:
            coupon = Coupen.objects.get(id=order.coupon_id)
        except:
            coupon = None

        return render(request, 'admin/view_order_admin.html', {'order': order, 'products': products, 'coupon': coupon})
    else:
        return redirect(admin_login)


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def sales(request):
    if 'admin_id' in request.session:

        return render(request, 'admin/sales.html')
    else:
        return redirect(admin_login)


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def sales_report_custom(request):
    if 'admin_id' in request.session:

        startdate = request.GET['startdate']

        enddate = request.GET['enddate']

        if startdate == '' or enddate == '' or (startdate == '' and enddate == ''):
            messages.error(request, 'Select corresponding dates')
            return redirect(sales)
        order_today = OrderTable.objects.filter(date_delivered__gte=startdate, date_delivered__lte=enddate,
                                                status='Delivered').order_by('id')
        revenue = 0

        print(order_today)
        for i in order_today:
            revenue = i.amount + revenue

        return render(request, 'admin/sales_report_custom.html',
                      {'order_today': order_today, 'revenue': revenue, 'startdate': startdate, 'enddate': enddate})
    else:
        return redirect(admin_login)


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def sales_report(request):
    if 'admin_id' in request.session:

        order_today = OrderTable.objects.filter(date_delivered=datetime.date.today(), status='Delivered').order_by('id')

        revenue = 0

        p = Paginator(order_today, 7)
        page_num = request.GET.get('page', 1)

        # print("NUMBER OF PAGES")
        # print(p.num_pages)
        try:

            page = p.page(page_num)
        except EmptyPage:
            page = p.page(1)
        # print(page)

        print(order_today)
        for i in order_today:
            revenue = i.amount + revenue

        return render(request, 'admin/sales_report.html', {'order_today': order_today, 'revenue': revenue})
    else:
        return redirect(admin_login)


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def sales_report_weekly(request):
    if 'admin_id' in request.session:

        some_day_last_week = datetime.date.today() - datetime.timedelta(days=7)

        order_today = OrderTable.objects.filter(date_delivered__gte=some_day_last_week,
                                                date_delivered__lte=datetime.date.today(), status='Delivered').order_by(
            'id')

        p = Paginator(order_today, 7)
        page_num = request.GET.get('page', 1)

        # print("NUMBER OF PAGES")
        # print(p.num_pages)
        try:

            page = p.page(page_num)
        except EmptyPage:
            page = p.page(1)
        # print(page)

        print(some_day_last_week)
        # OrderTable.objects.filter(date_delivered = datetime. date. today() )
        revenue = 0
        # print(order_today)
        for i in order_today:
            revenue = i.amount + revenue

        return render(request, 'admin/sales_report_weekly.html', {'order_today': order_today, 'revenue': revenue})
    else:
        return redirect(admin_login)


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def sales_report_yearly(request):
    if 'admin_id' in request.session:

        some_day_last_week = datetime.date.today() - datetime.timedelta(days=365)

        order_today = OrderTable.objects.filter(date_delivered__gte=some_day_last_week,
                                                date_delivered__lte=datetime.date.today(), status='Delivered').order_by(
            'id')

        p = Paginator(order_today, 7)
        page_num = request.GET.get('page', 1)

        # print("NUMBER OF PAGES")
        # print(p.num_pages)
        try:

            page = p.page(page_num)
        except EmptyPage:
            page = p.page(1)
        # print(page)
        print(some_day_last_week)
        # OrderTable.objects.filter(date_delivered = datetime. date. today() )
        revenue = 0
        # print(order_today)
        for i in order_today:
            revenue = i.amount + revenue

        return render(request, 'admin/sales_report_yearly.html', {'order_today': order_today, 'revenue': revenue})
    else:
        return redirect(admin_login)

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def export_csv_yearly(request):
    if 'admin_id' in request.session:
        some_day_last_week = datetime.date.today() - datetime.timedelta(days=365)

        orders = OrderTable.objects.filter(date_delivered__gte=some_day_last_week,
                                           date_delivered__lte=datetime.date.today(), status='Delivered').order_by('id')

        response = HttpResponse(content_type="text/csv")
        response['Content-Disposition'] = 'attachment; filename=Orders' + \
                                          str(datetime.datetime.now()) + '.csv'

        writer = csv.writer(response)

        writer.writerow(
            ['Order Id', 'Amount', 'Name', 'Phone number', "Payment method" 'Ordered date', 'Delivereed Date'])

        for order in orders:
            writer.writerow(
                [order.id, order.amount, order.name, order.phone_number, order.payment_method, order.created_at,
                 order.date_delivered])

        return response
    else:
        return redirect(admin_login)

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def export_csv_weekly(request):
    if 'admin_id' in request.session:
        some_day_last_week = datetime.date.today() - datetime.timedelta(days=7)

        orders = OrderTable.objects.filter(date_delivered__gte=some_day_last_week,
                                           date_delivered__lte=datetime.date.today(), status='Delivered').order_by('id')

        response = HttpResponse(content_type="text/csv")
        response['Content-Disposition'] = 'attachment; filename=Orders' + \
                                          str(datetime.datetime.now()) + '.csv'

        writer = csv.writer(response)

        writer.writerow(
            ['Order Id', 'Amount', 'Name', 'Phone number', "Payment method" 'Ordered date', 'Delivereed Date'])

        for order in orders:
            writer.writerow(
                [order.id, order.amount, order.name, order.phone_number, order.payment_method, order.created_at,
                 order.date_delivered])

        return response
    else:
        return redirect(admin_login)

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def export_csv_daily(request):
    if 'admin_id' in request.session:

        orders = OrderTable.objects.filter(date_delivered=datetime.date.today(), status='Delivered').order_by('id')

        response = HttpResponse(content_type="text/csv")
        response['Content-Disposition'] = 'attachment; filename=Orders' + \
                                          str(datetime.datetime.now()) + '.csv'

        writer = csv.writer(response)

        writer.writerow(
            ['Order Id', 'Amount', 'Name', 'Phone number', "Payment method" 'Ordered date', 'Delivereed Date'])

        for order in orders:
            writer.writerow(
                [order.id, order.amount, order.name, order.phone_number, order.payment_method, order.created_at,
                 order.date_delivered])

        return response
    else:
        return redirect(admin_login)

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def export_csv_custom(request):
    if 'admin_id' in request.session:

        startdate = request.GET['startdate']

        enddate = request.GET['enddate']

        orders = OrderTable.objects.filter(date_delivered__gte=startdate, date_delivered__lte=enddate,
                                           status='Delivered').order_by('id')

        response = HttpResponse(content_type="text/csv")
        response['Content-Disposition'] = 'attachment; filename=Orders' + \
                                          str(datetime.datetime.now()) + '.csv'

        writer = csv.writer(response)

        writer.writerow(
            ['Order Id', 'Amount', 'Name', 'Phone number', "Payment method" 'Ordered date', 'Delivereed Date'])

        for order in orders:
            writer.writerow(
                [order.id, order.amount, order.name, order.phone_number, order.payment_method, order.created_at,
                 order.date_delivered])

        return response
    else:
        return redirect(admin_login)

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def export_excel_yearly(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename=Orders' + \
                                      str(datetime.datetime.now()) + '.xls'
    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Sales')
    row_num = 0
    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = ['Order Id', 'Amount', 'Name', 'Phone number', "Payment method" 'Ordered date', 'Delivereed Date']

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)
    font_style = xlwt.XFStyle()

    some_day_last_week = datetime.date.today() - datetime.timedelta(days=365)

    rows = OrderTable.objects.filter(date_delivered__gte=some_day_last_week, date_delivered__lte=datetime.date.today(),
                                     status='Delivered').values_list('id', 'amount', 'name', 'phone_number',
                                                                     'payment_method', 'created_at', 'date_delivered')

    for row in rows:
        row_num += 1

        for col_num in range(len(row)):
            ws.write(row_num, col_num, str(row[col_num]), font_style)
    wb.save(response)
    return response

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def export_excel_daily(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename=Orders' + \
                                      str(datetime.datetime.now()) + '.xls'
    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Sales')
    row_num = 0
    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = ['Order Id', 'Amount', 'Name', 'Phone number', "Payment method" 'Ordered date', 'Delivereed Date']

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)
    font_style = xlwt.XFStyle()

    rows = OrderTable.objects.filter(date_delivered=datetime.date.today(), status='Delivered').values_list('id',
                                                                                                           'amount',
                                                                                                           'name',
                                                                                                           'phone_number',
                                                                                                           'payment_method',
                                                                                                           'created_at',
                                                                                                           'date_delivered')

    for row in rows:
        row_num += 1

        for col_num in range(len(row)):
            ws.write(row_num, col_num, str(row[col_num]), font_style)
    wb.save(response)
    return response

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def export_excel_weekly(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename=Orders' + \
                                      str(datetime.datetime.now()) + '.xls'
    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Sales')
    row_num = 0
    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = ['Order Id', 'Amount', 'Name', 'Phone number', "Payment method" 'Ordered date', 'Delivereed Date']

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)
    font_style = xlwt.XFStyle()

    some_day_last_week = datetime.date.today() - datetime.timedelta(days=7)

    rows = OrderTable.objects.filter(date_delivered__gte=some_day_last_week, date_delivered__lte=datetime.date.today(),
                                     status='Delivered').values_list('id', 'amount', 'name', 'phone_number',
                                                                     'payment_method', 'created_at', 'date_delivered')

    for row in rows:
        row_num += 1

        for col_num in range(len(row)):
            ws.write(row_num, col_num, str(row[col_num]), font_style)
    wb.save(response)
    return response

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def export_excel_custom(request):
    startdate = request.GET['startdate']

    enddate = request.GET['enddate']

    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename=Orders' + \
                                      str(datetime.datetime.now()) + '.xls'
    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Sales')
    row_num = 0
    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = ['Order Id', 'Amount', 'Name', 'Phone number', "Payment method" 'Ordered date', 'Delivereed Date']

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)
    font_style = xlwt.XFStyle()

    some_day_last_week = datetime.date.today() - datetime.timedelta(days=7)

    rows = OrderTable.objects.filter(date_delivered__gte=startdate, date_delivered__lte=enddate,
                                     status='Delivered').values_list('id', 'amount', 'name', 'phone_number',
                                                                     'payment_method', 'created_at', 'date_delivered')

    for row in rows:
        row_num += 1

        for col_num in range(len(row)):
            ws.write(row_num, col_num, str(row[col_num]), font_style)
    wb.save(response)
    return response


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def offers(request):
    products = Product.objects.exclude(offer=0)

    print(id)
    return render(request, 'admin/offers.html', {'products': products})


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def add_new_product_offer(request):
    products = Product.objects.filter(offer=0)
    if request.method == 'POST':

        offer = request.POST['offer']
        id = request.POST['product']

        if offer == '' or int(offer) < 0 or int(offer) > 100:
            messages.error(request, 'Offer must be between 1 and 100', extra_tags='productadderror')
        elif id == '':
            messages.error(request, 'select a product', extra_tags='productadderror')
        else:

            Product.objects.filter(id=id).update(offer=offer)

            messages.success(request, 'Offer added sucessfully', extra_tags='productadderror')
            return redirect(offers)

    return render(request, 'admin/add_productoffer.html', {'products': products})


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def delete_product_offer(request, id):
    product = Product.objects.filter(id=id).update(offer=0)

    return redirect(offers)


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def delete_category_offer(request, id):
    product = Category.objects.filter(id=id).update(offer=0)

    return redirect(category_offers)


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def edit_prduct_offer(request, id):
    products = Product.objects.all()
    product = Product.objects.get(id=id)
    print(id)
    return render(request, 'admin/edit_prduct_offer.html', {'product': product, 'products': products})


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def category_offers(request):
    cat = Category.objects.exclude(offer=0)

    print(id)
    return render(request, 'admin/category_offers.html', {'products': cat})


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def add_new_category_offer(request):
    cat = Category.objects.filter(offer=0)

    if request.method == 'POST':

        offer = request.POST['offer']
        id = request.POST['product']

        if offer == '' or int(offer) < 0 or int(offer) > 100:
            messages.error(request, 'Offer must be between 1 and 100', extra_tags='productadderror')
        elif id == '':
            messages.error(request, 'select a category', extra_tags='productadderror')
        else:

            Category.objects.filter(id=id).update(offer=offer)

            messages.success(request, 'Offer added sucessfully', extra_tags='productadderror')
            return redirect(category_offers)

    return render(request, 'admin/add_new_category_offer.html', {'cat': cat})


# =========================================
# ==========Coupon==========================
from adminapp.models import Coupen


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def coupons(request):
    if 'admin_id' in request.session:
        coupon = Coupen.objects.all()
        print(coupon)
        return render(request, "admin/coupons.html", {'coupon': coupon})
    else:
        return redirect(admin_login)


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def delete_coupon(request, id):
    coupon = Coupen.objects.get(id=id)
    coupon.delete()

    return redirect(coupons)


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def add_coupon(request):
    import string
    import random
    N = 9
    res = ''.join(random.choices(string.ascii_uppercase +
                                 string.digits, k=N))
    if 'admin_id' in request.session:
        if request.method == 'POST':
            code = request.POST['code']
            minimum = request.POST['minimum']
            discount = request.POST['discount']
            # initializing size of string

            # using random.choices()
            # generating random strings
            res = ''.join(random.choices(string.ascii_uppercase +
                                         string.digits, k=N))

            while Coupen.objects.filter(coupen_code=str(res)) is None:
                res = ''.join(random.choices(string.ascii_uppercase +
                                             string.digits, k=N))
                # tracking_no=tracking_no
            print(res)
            # print result
            print("The generated random string : " + str(res))

            Coupen.objects.create(coupen_code=code, minimum_amount=minimum, discount_price=discount)
        return render(request, "admin/add_coupon.html", {'code': str(res)})
    else:
        return redirect(admin_login)


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def update_coupon(request, id):
    if 'admin_id' in request.session:
        coupon = Coupen.objects.get(id=id)
        if request.method == 'POST':
            discount = request.POST['discount']
            minimum = request.POST['minimum']

            coupon = Coupen.objects.filter(id=id).update(discount_price=discount, minimum_amount=minimum)

            messages.success(request, 'Coupon updated sucessfully', extra_tags='productadderror')

        cat = Category.objects.all()
        return render(request, 'admin/update_coupon.html', {'coupon': coupon})

    else:
        return redirect(admin_login)


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def update_product_offer(request, id):
    if 'admin_id' in request.session:
        product = Product.objects.get(id=id)
        if request.method == 'POST':
            offer = request.POST['offer']

            if offer == '' or int(offer) < 0 or int(offer) > 100:
                messages.error(request, 'Offer must be between 1 and 100', extra_tags='productadderror')
            else:

                Product.objects.filter(id=id).update(offer=offer)

                messages.success(request, 'Offer updated sucessfully', extra_tags='productadderror')
                return redirect(offers)
        cat = Category.objects.all()
        return render(request, 'admin/update_product_offer.html', {'product': product})

    else:
        return redirect(admin_login)


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def update_category_offer(request, id):
    if 'admin_id' in request.session:
        # product = Category.objects.get(id=id)
        if request.method == 'POST':
            offer = request.POST['offer']

            if offer == '' or int(offer) < 0 or int(offer) > 100:
                messages.error(request, 'Offer must be between 1 and 100', extra_tags='productadderror')
            else:

                Category.objects.filter(id=id).update(offer=offer)

                messages.success(request, 'Offer updated sucessfully', extra_tags='productadderror')
                return redirect(category_offers)
        cat = Category.objects.get(id=id)
        return render(request, 'admin/update_category_offer.html', {'product': cat})

    else:
        return redirect(admin_login)

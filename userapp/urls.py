from django.urls import path, include
from . import views


urlpatterns = [
    # product view and home urls 

    path('', views.landing, name=''),
    path('user_home/', views.user_home, name=''),
    path('user_login/', views.user_login, name='user_login'),
    path('otp_login/', views.otp_login, name='otp_login'),
    path('otp_confirm/', views.otp_confirm, name='otp_login'),
    path('user_signup/', views.user_signup, name='user_signup'),
    path('user_logout/', views.user_logout, name='user_logout'),
    path('shop/', views.shop, name='shop'),
    path('product_view/<int:id>', views.product_view, name='shop'),
    path('category_list/<int:id>', views.category_list, name='category_list'),
    #search
    path('search_results', views.search_results, name='search_results'),
    
    
    # cart Management urls
    path('cartview/', views.cartview, name='shop'),
    path('add_cart/<int:id>', views.add_cart, name='shop'), 
    path('add_cart_product_view/<int:id>', views.add_cart_product_view, name='add_cart_product_view'),
    path('plus_cart_quantity/<int:quantity>/<int:id>', views.plus_cart_quantity, name='plus_cart_quantity'),
    path('minus_cart_quantity/<int:quantity>/<int:id>', views.minus_cart_quantity, name='minus_cart_quantity'),
    path('update_quantity/<int:id>', views.update_quantity, name='update_quantity'),
    
    path('delete_product_cart/<int:id>', views.delete_product_cart, name='delete_product_cart'), 
    path('delete_cart', views.delete_cart, name='delete_cart'), 


    
    # Order management Urls
    path('choose_address_select/', views.choose_address_select, name='choose_address_select'), 
    path('choose_address/', views.choose_address, name='choose_address'), 
    path('choose_payment_method/<int:id>', views.choose_payment_method, name='choose_payment_method'), 
    path('update_address/<int:id>/', views.update_address, name='choose_address'), 
    path('create_order/<int:id>', views.create_order, name='create_order'), 
    
    path('choose_payment/', views.choose_payment, name='choose_payment'), 
    
    path('order_user/', views.order_user, name='order_user'),
    path('active_orders/', views.active_orders, name='active_orders'), 
    path('active_order_products/<int:id>', views.active_order_products, name='active_order_products'), 
    path('order_cancel_user/<int:id>', views.order_cancel_user, name='order_cancel_user'), 
    path('razorpay_pay/<int:amount>', views.razorpay_pay, name='razorpay_pay'), 
    path('razorpay_success/', views.razorpay_success, name='razorpay_success'), 
    path('paypal/<int:amount>', views.paypal, name='paypal'), 
    path('paypalsuccess/', views.paypalsuccess, name='paypalsuccess'),
    path('payment_failed/', views.payment_failed, name='payment_failed'), 
    path('payment_success_page/', views.payment_success_page, name='payment_success_page'), 
    
    path('cod_success/', views.cod_success, name='cod_success'), 
    
    path('delivered_orders/', views.delivered_orders, name='delivered_orders'), 
    path('return_order/<int:id>', views.return_order, name='return_order'), 
    path('view_order_user/<int:id>', views.view_order_user, name='view_order_user'), 
    
    
    # user profile 

    path('userprofile/', views.userprofile, name='userprofile'), 
    path('add_address/', views.add_address, name='add_address'), 
    path('update_address_user/<int:id>/', views.update_address_user, name='update_address_user'), 
    path('delete_address_user/<int:id>/', views.delete_address_user, name='delete_address_user'), 
    path('wallet/', views.wallet, name='wallet'), 
    
    
    # coupon====
    path('apply_coupon/<int:id>', views.apply_coupon, name='apply_coupon'),
    
    # guest uset ===================================
    path('guest_user/', views.guest_user, name='guest_user'),
    path('test', views.test, name='test'),
    
    
    
]
from django.urls import path, include
from . import views


urlpatterns = [
    
    path('admin_login/', views.admin_login, name='admin_login'),
    path('admin_logout/', views.admin_logout, name='admin_login'),
    path('admin_home/', views.admin_home, name='admin_home'),
    
    
    
    path('customers/', views.customers, name='customers'),
    path('block/<int:id>/', views.block, name='block'),
    path('blocked_customers/', views.blocked_customers, name='blocked_customers'),
    path('unblock/<int:id>/', views.unblock, name='unblock'),
    path('view_customer/<int:id>/', views.view_customer, name='view_customer'),
    
    
    path('products/', views.products, name='products'),
    path('add_product/', views.add_product, name='add_product'),
    path('view_product/<int:id>/', views.view_product, name='view_product'),

    
    path('delete_category/<int:id>', views.delete_category, name='delete_category'),
    path('categories/', views.categories, name='categories'),
    path('add_category/', views.add_category, name='add_category'),
    path('edit_category/<int:id>', views.edit_category, name='edit_category'),
    path('view_category/<int:id>', views.view_category, name='view_category'),

    
    
    #path('add_product/', views.add_product, name='add_product'),
    path('delete_product/<int:id>', views.delete_product, name='delete_product'),
    path('update_product/<int:id>', views.update_product, name='update_product'),   
    
    path('orders/', views.orders, name='orders'), 
    path('order_list/', views.order_list, name='order_list'),  
    path('order_accept/<int:id>', views.order_accept, name='order_accept'),  
    path('order_reject/<int:id>', views.order_reject, name='order_reject'),  
    path('order_view/', views.order_view, name='order_view'),   
    path('order_delivery/', views.order_delivery, name='order_delivery'),  
    path('order_delivered/<int:id>', views.order_delivered, name='order_delivered'),
    path('view_order_admin/<int:id>', views.view_order_admin, name='view_order_admin'),

    
    
    path('edit_prduct_offer/<int:id>', views.edit_prduct_offer, name='edit_prduct_offer'),
    path('offers/', views.offers, name='offers'),
    path('coupons/', views.coupons, name='coupons'),
    path('add_coupon/', views.add_coupon, name='add_coupon'),
    path('delete_coupon/<int:id>', views.delete_coupon, name='delete_coupon'),
    path('update_coupon/<int:id>', views.update_coupon, name='update_coupon'),
    path('update_product_offer/<int:id>', views.update_product_offer, name='update_product_offer'),
    path('add_new_product_offer', views.add_new_product_offer, name='add_new_product_offer'),
    path('delete_product_offer/<int:id>', views.delete_product_offer, name='delete_product_offer'),
    path('delete_category_offer/<int:id>', views.delete_category_offer, name='delete_category_offer'),
    path('category_offers/', views.category_offers, name='category_offers'),
    path('add_new_category_offer', views.add_new_category_offer, name='add_new_category_offer'),
    path('update_category_offer/<int:id>', views.update_category_offer, name='update_category_offer'),
    
    
    path('sales/', views.sales, name='sales'),
    path('sales_report/', views.sales_report, name='sales_report'),
    path('sales_report_weekly/', views.sales_report_weekly, name='sales_report_weekly'),
    path('sales_report_yearly/', views.sales_report_yearly, name='sales_report_yearly'),
    path('sales_report_custom/', views.sales_report_custom, name='sales_report_custom'),
    
    path('export_csv_yearly/', views.export_csv_yearly, name='export_csv_yearly'),
    path('export_csv_weekly/', views.export_csv_weekly, name='export_csv_weekly'),
    path('export_csv_daily/', views.export_csv_daily, name='export_csv_daily'),
    path('export_csv_custom/', views.export_csv_custom, name='export_csv_custom'),
    
    path('export_excel_yearly/', views.export_excel_yearly, name='export_excel_yearly'),
    
    
    path('export_excel_daily/', views.export_excel_daily, name='export_excel_daily'),
    path('export_excel_weekly/', views.export_excel_weekly, name='export_excel_weekly'),
    path('export_excel_custom/', views.export_excel_custom, name='export_excel_custom'),
    
    
    
]
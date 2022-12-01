from django.urls import path

from .import views

app_name = 'cart'
urlpatterns = [
    # path('cart/', views.cart_deatil, name='cart'),
    # path('add/<int:product_id>/', views.cart_deatil, name='cart_add'),
    # path('remove/<int:product_id>/', views.cart_deatil, name='cart_deatil'),
    path('test/', views.test, name='test'),
    path('create/', views.create, name='test'),


    
]

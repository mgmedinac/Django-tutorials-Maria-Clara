from django.urls import path
from .views import (
    CartView,
    Contactview,
    HomePageView,
    AboutPageView,
    ProductIndexView,
    ProductShowView,
    ProductCreateView,
    CartRemoveAllView,
    Contactview
)



urlpatterns = [
    path('', HomePageView.as_view(), name='home'),  
    path('about/', AboutPageView.as_view(), name='about'),
    path('contact/', Contactview.as_view(), name='contact'),
    path('products/', ProductIndexView.as_view(), name='products'),
    path('products/<str:id>', ProductShowView.as_view(), name='show'),
    path('products/create/', ProductCreateView.as_view(), name='product-create'),
    path('products/created/', HomePageView.as_view(), name='product-created'), 
    path('cart/', CartView.as_view(), name='cart_index'),
    path('cart/add/<str:product_id>', CartView.as_view(), name='cart_add'),
    path('cart/removeAll', CartRemoveAllView.as_view(), name='cart_removeAll'),
]

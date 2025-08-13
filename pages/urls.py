from django.urls import path
from django.views.generic import TemplateView

from .views import (
    CartView,
    Contactview,
    HomePageView,
    AboutPageView,
    ProductIndexView,
    ProductShowView,
    ProductCreateView,
    CartRemoveAllView,
    Contactview,
    
)
from .views import ImageViewFactory
from .utils import ImageLocalStorage



urlpatterns = [
    path('', HomePageView.as_view(), name='home'),  
    path('about/', AboutPageView.as_view(), name='about'),
    path('contact/', Contactview.as_view(), name='contact'),
    path('products/', ProductIndexView.as_view(), name='products'),
    path('products/<str:id>', ProductShowView.as_view(), name='show'),
    path('products/create/', ProductCreateView.as_view(), name='product-create'),
    path('products/created/', TemplateView.as_view(template_name='products/productCreated.html'), name='product-created'),
    path('cart/', CartView.as_view(), name='cart_index'),
    path('cart/add/<str:product_id>', CartView.as_view(), name='cart_add'),
    path('cart/removeAll', CartRemoveAllView.as_view(), name='cart_removeAll'),
    path('image/', ImageViewFactory(ImageLocalStorage()).as_view(), name='image_index'),
    path('image/save', ImageViewFactory(ImageLocalStorage()).as_view(), name='image_save'),
    
]

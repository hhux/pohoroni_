from django.urls import path

from .views import test_view, ProductDetailView, info_view, items_view, services_view

""""Прописываем маршруты (связываем вьюхи с урлами"""
urlpatterns = [
    path('', test_view, name='base'),
    path('products/<str:ct_model>/<str:slug>/', ProductDetailView.as_view(), name='product_detail'),
    path('info/', info_view, name='info'),
    path('items/', items_view, name='items'),
    path('services/', services_view, name='services')
]


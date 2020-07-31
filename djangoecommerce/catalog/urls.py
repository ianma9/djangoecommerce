from django.urls import path

from . import views

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('<slug>/', views.category, name='category'),
    path('produtos/<slug>/', views.product, name='product'),
]

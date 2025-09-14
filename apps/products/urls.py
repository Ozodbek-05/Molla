from django.urls import path
from apps.products.views import product_lis_view

app_name = 'products'

urlpatterns = [
    path('', product_lis_view, name='list')
]

from django.urls import path
from apps.products.views import ProductsView, ProductDetailView

app_name = 'products'

urlpatterns = [
    path('', ProductsView.as_view(), name='list'),
    path('<int:pk>/', ProductDetailView.as_view(), name='detail'),
]

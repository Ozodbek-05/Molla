from django.shortcuts import render

def product_lis_view(request):
    return render(request, 'products/products.html')


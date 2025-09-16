from django.views.generic import DetailView
from django.views.generic.list import ListView
from django.db.models import Count, Q
from apps.products.models import ProductCategory, ProductModel, ProductSize, ProductColor, ProductBrand, ProductQuantity


class ProductsView(ListView):
    model = ProductModel
    template_name = "products/products.html"
    context_object_name = "products"

    def get_queryset(self):
        context = ProductModel.objects.all()
        cat_id = self.request.GET.get('cat')
        quantity_id = self.request.GET.get('quantity_id')
        brand_id = self.request.GET.get('brand_id')
        color_id = self.request.GET.get('color_id')
        size_id = self.request.GET.get('size_id')
        q = self.request.GET.get('q')

        if cat_id:
            context = context.filter(categories=cat_id)
        if quantity_id:
            context = context.filter(quantity=quantity_id)
        if brand_id:
            context = context.filter(brand=brand_id)
        if color_id:
            context = context.filter(products_quantity__color=color_id)
        if size_id:
            context = context.filter(products_quantity__size=size_id)
        if q:
            context = context.filter(title__icontains=q)

        return context.distinct()

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["categories"] = ProductCategory.objects.all()
        context["quantity"] = ProductQuantity.objects.all()
        context["brand"] = ProductBrand.objects.all()
        context["colors"] = ProductColor.objects.all()
        context["sizes"] = ProductSize.objects.all()

        context["most_popular_products"] = (
            ProductModel.objects
            .annotate(views_count=Count('views', distinct=True))
            .order_by('-views_count')[:4]
        )
        return context

class ProductDetailView(DetailView):
    model = ProductModel
    template_name = "products/product_detail.html"
    context_object_name = "product"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["related_products"] = (
            ProductModel.objects
            .filter(categories__in=self.object.categories.all())
            .exclude(id=self.object.id)
            .distinct()[:4]
        )
        return context
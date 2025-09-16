import threading
from django.db.models import Count
from django.views.generic import ListView, DetailView
from apps.blogs.models import BlogModel, BlogCategoryModel, BlogTagModel
from apps.blogs.utils import check_blog_view


class BlogListView(ListView):
    template_name = 'blogs/blog-list.html'

    def get_queryset(self):
        return BlogModel.objects.filter(
            status=BlogModel.BlogStatus.PUBLISHED
        )

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        categories = BlogCategoryModel.objects.all()
        tags = BlogTagModel.objects.all()
        most_popular_blogs = (
            BlogModel.objects
            .annotate(views_count=Count('views', distinct=True))
            .order_by('-views_count')[:4]
        )
        context["blogs"] = self.get_queryset()
        context["categories"] = categories
        context["tags"] = tags
        context["most_popular_blogs"] = most_popular_blogs

        return context


class BlogDetailView(DetailView):
    template_name = 'blogs/blog-detail.html'
    queryset = BlogModel.objects.all()
    context_object_name = 'blog'
    pk_url_kwarg = 'pk'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        blog = self.get_object()

        # update view count of blog
        threading.Thread(target=check_blog_view, args=(self.request, blog,)).start()

        categories = BlogCategoryModel.objects.all()
        tags = BlogTagModel.objects.all()
        related_blogs = BlogModel.objects.filter(
            category__in=blog.category.all()
        ).exclude(id=blog.id).distinct()
        most_popular_blogs = (
            BlogModel.objects
            .annotate(views_count=Count('views', distinct=True))
            .order_by('-views_count')[:4]
        )

        context["blogs"] = self.get_queryset()
        context["categories"] = categories
        context["tags"] = tags
        context["most_popular_blogs"] = most_popular_blogs
        context["related_blogs"] = related_blogs

        return context

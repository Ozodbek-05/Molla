from django.shortcuts import render


def blogs_list_view(request):
    return render(request, 'blogs/blog-list.html')

def blogs_detail_view(request):
    return render(request, 'blogs/blog-detail.html')
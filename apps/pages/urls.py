from django.urls import path

from apps.pages.views import home_page_view, contact_page_view

app_name = 'pages'

urlpatterns = [
    path('contact/', contact_page_view, name='contact'),
    path('about/', contact_page_view, name='about'),
    path('', home_page_view, name='home'),
]

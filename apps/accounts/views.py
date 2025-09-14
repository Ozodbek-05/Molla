from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views.generic import CreateView

from apps.accounts.forms import RegisterModelForm


class RegisterCreateView(CreateView):
    model = User
    form_class = RegisterModelForm
    template_name = 'auth/login.html'
    success_url = reverse_lazy('pages:home')

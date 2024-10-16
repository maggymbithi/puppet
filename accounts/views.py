from django.shortcuts import render
from .forms import CustomUserCreationForn
from django.urls import reverse_lazy
from django.views.generic import CreateView

class SignupView(CreateView):
    form_class=CustomUserCreationForn
    success_url=reverse_lazy('login')
    template_name='registration/signup.html'
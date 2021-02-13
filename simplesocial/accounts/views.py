from django.shortcuts import render
from django.urls import reverse_lazy
from . import forms
from django.views.generic import CreateView

# Create your views here.
class SignUp(CreateView):
    form_class = forms.UserCreateForm
    success_url = reverse_lazy('login') #reverse_lazy wait for successful signup while normal reverse just take you to the login
    template_name = 'accounts/signup.html'

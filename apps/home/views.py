from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from django.views.generic import TemplateView

class indexView(TemplateView):
    template_name = 'index.html'


class homePage(LoginRequiredMixin, TemplateView):
    template_name = "home/panelUsuario.html"
    login_url = reverse_lazy('user_app:login-register')


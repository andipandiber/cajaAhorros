from django.shortcuts import render
from django.urls import reverse_lazy

from django.contrib.auth.mixins import LoginRequiredMixin

from django.views.generic import CreateView, ListView, UpdateView, DeleteView, TemplateView

from .models import Role

class baseView(LoginRequiredMixin, TemplateView):
  template_name = 'role/inicio.html'
  login_url = reverse_lazy('user_app:login-user')

class createRoleView(LoginRequiredMixin,CreateView):
    model = Role
    template_name = "role/create.html"
    fields = ('__all__')
    success_url = reverse_lazy('role_app:base')
    login_url = reverse_lazy('user_app:login-user')

    def form_valid(self, form):
        role = form.save(commit = False)
        role.save()
        return super(createRoleView, self).form_valid(form)

class updateRoleView(LoginRequiredMixin, UpdateView):
    template_name = "role/update.html"
    model = Role
    fields = ('__all__')
    success_url = '/'
    login_url = reverse_lazy('user_app:login-user')

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        return super(updateRoleView, self).form_valid(form)

class deleteRoleView(LoginRequiredMixin, DeleteView):
    model = Role
    template_name = "role/delete.html"
    success_url = '/'
    login_url = reverse_lazy('user_app:login-user')

class listRoleView(LoginRequiredMixin, ListView):
    template_name = "role/list_all.html"
    context_object_name = 'roles'
    login_url = reverse_lazy('user_app:login-user')

    def get_queryset(self):
        key = self.request.GET.get("key", '')
        list = Role.objects.filter(
            name_role__icontains = key
        )
        return list






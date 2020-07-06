from django.shortcuts import render

from django.views.generic import CreateView, ListView, UpdateView, DeleteView

from .models import Role


class create_role(CreateView):
    template_name = "role/new_role.html"
    model = Role
    fields = ('__all__')

    def form_valid(self, form):
        role = form.save(commit = False)
        role.save
        return super().form_valid(form)

class list_all_role(ListView):
    template_name = "role/list_all.html"
    model = Role
    context_object_name = 'lista_roles'

    def get_queryset(self):
        key = self.request.GET.get("kword", '')
        return Role.objects.search_role(key)

class list_key_role(ListView):
    template_name = "role/lista_by_key.html"
    context_object_name = 'lista_roles'

    def get_queryset(self):
        key = self.request.GET.get("busca", '')
        list = Role.objects.filter(
            name_role = key
        )
        return list

class delete_role(DeleteView):
    template_name = "role/delete_role.html"
    model = Role

class update_role(UpdateView):
    template_name = "role/update_role.html"
    model = Role
    fields = ('__all__')

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        request.POST
        request.POST['name_role']
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        return super(update_role, self).form_valid(form)

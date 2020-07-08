from django.shortcuts import render

from django.views.generic import CreateView, ListView, UpdateView, DeleteView

from .models import Role


class createRoleView(CreateView):
    model = Role
    template_name = "role/create.html"
    fields = ('__all__')
    success_url = '/'

    def form_valid(self, form):
        role = form.save(commit = False)
        role.save()
        return super(createRoleView, self).form_valid(form)

class updateRoleView(UpdateView):
    template_name = "role/update.html"
    model = Role
    fields = ('__all__')
    success_url = '/'

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        return super(updateRoleView, self).form_valid(form)

class deleteRoleView(DeleteView):
    model = Role
    template_name = "role/delete.html"
    success_url = '/'

class listRoleView(ListView):
    template_name = "role/list_all.html"
    context_object_name = 'roles'

    def get_queryset(self):
        key = self.request.GET.get("key", '')
        list = Role.objects.filter(
            name_role__icontains = key
        )
        return list






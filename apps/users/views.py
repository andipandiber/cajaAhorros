from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, TemplateView, UpdateView, DeleteView, DetailView

from .models import Socio,Usuario

class base_view(TemplateView):
    template_name = 'inicio.html'

class list_all_users(ListView):
    template_name = "persona/list_all.html"
    paginate_by = 4
    ordering = 'codigo'
    context_object_name = 'users'

    def get_queryset(self):
        key = self.request.GET.get("key", '')
        list = Usuario.objects.filter(
             nombre__icontains= key
        )
        return list

class user_detail(DetailView):
    model = Usuario
    template_name = "persona/detail.html"

    def get_context_data(self, **kwargs):
        context = super(user_detail, self).get_context_data(**kwargs)
        context["titulo"] = "Empleado"
        return context
    
class list_by_roles(ListView):
    template_name = "persona/list_by_role.html"
    context_object_name = 'usersRoles'

    def get_queryset(self):

        area = self.kwargs['shortname']
        list = Usuario.objects.filter(
                role__name = area
        )

        return list

class list_by_key(ListView):
    template_name = "persona/list_by_key.html"
    context_object_name = 'users'

    def get_queryset(self):
        print('---------')
        key = self.request.GET.get("busca", '')
        print(key)
        list = Usuario.objects.filter(
             nombre= key
        )
        print('Lista Resultados ',list)
        return list

class success_View(TemplateView):
    template_name = "persona/success.html"

class create_User(CreateView):
    template_name = 'persona/create.html'
    model = Usuario
    success_url = reverse_lazy('user_app:inicio')

    # Logica del Proceso
    def form_valid(self, form):
        user = form.save(commit=False)
        user.save()
        return super(create_User, self).form_valid(form)

class update_user(UpdateView):
    model = Usuario
    template_name = "persona/update.html"
    fields = ('__all__')
    success_url = reverse_lazy('user_app:inicio')

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        print('---------Metodo Post----------------')
        print('------------------------------------')
        print(request.POST)
        print('------------------------------------')
        print(request.POST['nombre'])
        print('------------------------------------')
        return super().post(request, *args, **kwargs)


    def form_valid(self, form):
        print('---------Metodo Form-Valida---------')
        print('------------------------------------')

        return super(update_user, self).form_valid(form)

class delete_user(DeleteView):
    model = Usuario
    template_name = "persona/delete.html"
    success_url = reverse_lazy('user_app:inicio') 

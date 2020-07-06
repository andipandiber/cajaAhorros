from django.urls import path

from . import views

app_name = "role_app"

urlpatterns = [
    path('roles/', views.list_all_role.as_view(), name = "list_roles")
]
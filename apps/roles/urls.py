from django.urls import path

from . import views

app_name = "role_app"

urlpatterns = [
    path('inicio', views.baseView.as_view(), name = 'base'),
    path('createRole/', views.createRoleView.as_view(), name='create-Role'),
    path('listRole/', views.listRoleView.as_view(), name='list-Role'),
    path('updateRole/<pk>', views.updateRoleView.as_view(), name='update-Role'),
    path('deleteRole/<pk>', views.deleteRoleView.as_view(), name='delete-Role'),
]


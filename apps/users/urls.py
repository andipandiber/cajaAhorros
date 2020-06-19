from django.urls import path

from . import views

app_name = "user_app"

urlpatterns = [
    path('', views.base_view.as_view(), name='inicio'),
    path('listar/', views.list_all_users.as_view(), name='user_all'),
    path('detalle/<pk>', views.user_detail.as_view(), name='detail'),
    path('listar2/<shortname>', views.list_by_roles.as_view(), name='userRoles'),
    path('listar3/', views.list_by_key.as_view()),
    path('create/', views.create_User.as_view(), name='createUser'),
    path('success/', views.success_View.as_view(), name='creado'),
    path('update/<pk>', views.update_user.as_view(), name='updateUser'),
    path('delete/<pk>', views.delete_user.as_view(), name='deleteUser'),
]
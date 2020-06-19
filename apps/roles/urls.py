from . import views
from django.urls import path

app_name = "role_app"

urlpatterns = [
    path('', views.list_all_role.as_view(), name='list_all_role'),
    path('list/', views.list_key_role.as_view(), name='list_by_key'),
    path('new/', views.create_role.as_view(), name='create_role'),
    path('update/<pk>', views.update_role.as_view(), name='update_role'),
    path('delete/<pk>', views.delete_role.as_view(), name='delete_role'),
]
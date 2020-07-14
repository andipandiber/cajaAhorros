from django.urls import path


from . import views


app_name = "home_app"

urlpatterns = [
    path('', views.indexView.as_view(), name = 'index'),
    path('panel/', views.homePage.as_view(), name = 'panel'),
]


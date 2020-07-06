from django.urls import path

from . import views

app_name = "user_app"

urlpatterns = [
    path('create/', views.userRegisterView.as_view(), name='user-register'),
    path('login/', views.loginUserView.as_view(), name='login-register'),
    path('logout/', views.logoutUserView.as_view(), name='logout-register'),
    path('update/', views.updatePasswordView.as_view(), name='user-update'),
    path('user-verification/<pk>/', views.codeVerificationView.as_view(), name='user-verification'),
]

from django.urls import path


from . import views

app_name = "user_app"

urlpatterns = [
    path('create/', views.userRegisterView.as_view(), name='register-user'),
    path('login/', views.loginUserView.as_view(), name='login-user'),
    path('logout/', views.logoutUserView.as_view(), name='logout-user'),
    path('update/', views.updatePasswordView.as_view(), name='user-update'),
    path('user-verification/<pk>/', views.codeVerificationView.as_view(), name='user-verification'),
]

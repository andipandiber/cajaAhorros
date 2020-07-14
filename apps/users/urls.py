from django.urls import path


from . import views

app_name = "user_app"

urlpatterns = [
    path('create/', views.userRegisterView.as_view(), name='register-user'),
    path('login/', views.loginUserView.as_view(), name='login-user'),
    path('logout/', views.logoutUserView.as_view(), name='logout-user'),
    path('updatePassword/', views.updatePasswordView.as_view(), name='user-updatePassword'),
    path('updateUser/<pk>', views.updateUserView.as_view(), name='user-update'),
    path('deleteUser/<pk>', views.deleteUserView.as_view(), name='user-delete'),
    path('listUser/', views.listUserView.as_view(), name='user-list'),
    path('user-verification/<pk>/', views.codeVerificationView.as_view(), name='user-verification'),
]

from django.urls import path

from . import views

urlpatterns = [
    path('hello/', views.LoginifyView, name='hello'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_view, name='login'),
    path('users/', views.get_all_users, name='get_all_users'),
    path('user/<str:email>/', views.getUser_by_email, name='getUser_by_email'),
    path('user/update/<str:email>/', views.update_user, name='update_user'),
    path('user/delete/<str:email>/', views.delete_user, name='delete_user'),

]

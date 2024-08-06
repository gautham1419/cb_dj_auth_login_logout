from django.urls import path
from pages import views

urlpatterns = [
    path('', views.home,name='home'),
    path('login/register/',views.register_view,name='register'),
    path('accounts/login/register/', views.register_view, name='register'),
    path('buy/', views.buy_view, name='buy'),
    path('user/', views.user_view, name='user'),
]
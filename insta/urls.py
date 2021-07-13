from django.urls import path
from . import views

urlpatterns = [
    # auth urls
    path('register/', views.register_user, name='register'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),

    # user urls
    path('', views.home, name='home'),
]
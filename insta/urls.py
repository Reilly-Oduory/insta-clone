from django.urls import path
from . import views

urlpatterns = [
    # auth urls
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),

    # user urls
]
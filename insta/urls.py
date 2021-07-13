from django.urls import path
from . import views

urlpatterns = [
    # auth urls
    path('register/', views.register_user, name='register'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),

    # user urls
    path('', views.home, name='home'),

    # search users

    # profile urls
    path('add_profile/', views.create_profile, name='create_profile'),
    path('update_profile/', views.update_profile, name='update_profile'),
    path('profile/', views.view_profile, name='profile'),

    # post urls
    path('new_post/', views.new_post, name='new_post'),
    path('post/<post_id>/', views.view_post, name='post'),
    path('post/<post_id>/like/', views.like, name='post_like'),
    path('post/<post_id>/update/', views.update_post_caption, name='post_caption_update'),

    # comments
    path('post/<post_id>/comment/', views.new_comment, name='comment'),
]
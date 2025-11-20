from django.urls import path
from . import views

urlpatterns = [
    path('', views.hello_world, name='hello-world'),
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('api/users/', views.get_all_users, name='api-get-all-users'),
    path('api/users/<str:email>/', views.get_user_by_email, name='api-get-user'),
    path('api/users/<str:email>/update/', views.update_user, name='api-update-user'),
    path('api/users/<str:email>/delete/', views.delete_user, name='api-delete-user'),
]
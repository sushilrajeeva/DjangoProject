from django.urls import path
from . import views

urlpatterns = [
    path('', views.hello_world, name='hello-world'),
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
]
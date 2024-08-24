from . import views
from django.urls import path


urlpatterns = [
    path('', views.login_user, name='login-user'),
    path('logout_user', views.logout_user, name='logout-user'),
    path('sign-up', views.register, name='register'),
    path('send_email', views.send_email, name='send_email'),
     
]

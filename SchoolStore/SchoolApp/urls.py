from django.urls import path

from SchoolApp import views

urlpatterns = [
    path('', views.home,name='home'),
    path('login', views.login , name='login'),
    path('register', views.register, name='register'),
    path('info', views.info, name='info'),
    path('logout', views.logout, name='logout'),
    path('success', views.success, name='success'),

]

from django.urls import path
from . import views 

urlpatterns = [
    path('', views.BASE, name='BASE'),
    path('inicio/', views.inicio, name='inicio'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.signout, name='logout'),
    path('signin/', views.signin, name='signin'),
    path('situacion/', views.padron_situacion, name='padron_situacion'),
]

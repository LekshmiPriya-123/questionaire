from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('userregistration/',views.userregister,name='user'),
    path('login/',views.loginuser,name='login'),
    path('authuser/',views.userauth,name='authuser'),
    path('qns/',views.qnsgenerator,name='qns'),
    path('qnsdata/',views.qns_render,name="qnsdata"),
    path('logout/',views.logoutuser,name='logout'),
    path('answers/',views.answers,name='answers'),
]
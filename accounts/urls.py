from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name="home"),
    path('accounts/log/',views.login_view,name="login"),
    path('accounts/sign_up/',views.sign_up,name="sign-up"),
]
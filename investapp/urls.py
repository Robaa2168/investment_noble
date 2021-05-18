from django.urls import path, re_path, include
from . import views
from django.contrib.auth import views as auth_views
from investapp import views as user_views


urlpatterns=[
    path('index/ref=<ref>/',views.index,name = 'index'),
    # path('register/', views.registerPage, name="register"),
    # path('login/', views.loginPage, name="login"),
    # path('logout/', views.logoutUser, name="logout"),
    path("make-investment/",views.makeInvestment, name="makeinvetment")
]
from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name="index"),
    path('login',views.login,name="login"),
    path('home',views.home,name="home"),
    path('contact',views.contact,name="contact"),
    path('details',views.details,name="details")

]

from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name="HomePage"),
    path('home', views.index, name="HomePage"),
    path('deposit', views.addMoney, name="Adding balance"),
    path('withdraw', views.withdrawMoney, name="Withdrawing balance"),
    path('check', views.checkMoney, name="Checking  balance"),
    path('about', views.about, name="About"),
]
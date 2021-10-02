from django.urls import path
from . import views

urlpatterns = [
    path('', views.ninja_gold),
    path('process_money', views.process_money),
]
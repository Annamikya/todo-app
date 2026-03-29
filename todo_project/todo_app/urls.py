from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('complete/<int:id>/', views.complete_task),
    path('delete/<int:id>/', views.delete_task),
]
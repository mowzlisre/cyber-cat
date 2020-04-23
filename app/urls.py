from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('learn/<pk>/', views.classes, name='subject'),
    path('learn/<pk>/<int:id>/', views.tutorials, name='tutorial'),
]


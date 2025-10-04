from django.urls import path
from . import views

urlpatterns = [
    path('', views.eventos, name='eventos'),
    path('evento_exito/', views.evento_exito, name='evento_exito'),
]
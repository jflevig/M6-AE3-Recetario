from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('receta/<str:nombre>/', views.receta_detalle, name='receta_detalle'),
    path('contacto', views.contacto, name='contacto'),
    path('error/', views.Error, name="error"),
]

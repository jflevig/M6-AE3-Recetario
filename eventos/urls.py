from django.urls import path
from .import views
from django.contrib.auth import views as auth_views
#from .views import EliminarEvento y Editar evento 

urlpatterns = [
    path('', views.eventos, name='eventos'),
    path('evento_exito/', views.evento_exito, name='evento_exito'),
    path('lista_eventos/', views.lista_eventos, name='lista_eventos'), #2da parte del proyecto que muestra la lista de eventos registrados
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    #path('editar_evento/', EditarEvento.as_view(), name='editar_evento'),
    #path('eliminar_evento/', views.Eliminar_Evento, name='eliminar_evento'),

]

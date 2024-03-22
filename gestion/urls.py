from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView
from .views import PerfilUsuarioApiView, RegistroUsuarioApiView, RegistroPacienteApiView, RegistroCitaApiView, UnPacienteApiView, UnaCitaApiView


urlpatterns = [
    
    path('login', TokenObtainPairView.as_view()),
    path('perfil', PerfilUsuarioApiView.as_view()),
    path('registrousuario', RegistroUsuarioApiView.as_view()),
    path('registropaciente', RegistroPacienteApiView.as_view()),
    path('registrocita', RegistroCitaApiView.as_view()),
    path('paciente/<int:id>', UnPacienteApiView.as_view()),
    path('cita/<int:id>', UnaCitaApiView.as_view()),
    #path('detallecita', DetalleCitaApiView.as_view()),
    
    
]
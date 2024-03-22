from rest_framework import serializers
from .models import UsuarioModel, PacienteModel, CitaModel #, DetalleCitaModel

class RegistroUsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = UsuarioModel
        fields = '__all__'
        
class RegistroPacienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = PacienteModel
        fields = '__all__'
        
class RegistroCitaSerializer(serializers.ModelSerializer):
    class Meta:
        model = CitaModel
        fields = '__all__'
        
class MostrarUsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = UsuarioModel
        exclude = ['password','is_staff', 'user_permissions', 'groups', 'last_login', 'is_superuser']
        
class MostrarPacienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = PacienteModel
        exclude = ['registro','dni', 'apellido_paterno', 'apellido_materno', 'primer_nombre', 'segundo_nombre','sexo', 'lugar_nacimiento', 'fecha_nacimiento', 'grupo_sanguineo', 'rh', 'correo']
        

class MostrarCitaSerializer(serializers.ModelSerializer):
    class Meta:
        model = CitaModel
        fields = '__all__'
from rest_framework import generics, response, status, request, permissions
from .models import UsuarioModel, PacienteModel, CitaModel, DetalleCitaModel
from .serializers import RegistroUsuarioSerializer, MostrarUsuarioSerializer, RegistroPacienteSerializer, MostrarPacienteSerializer, RegistroCitaSerializer, MostrarCitaSerializer
from .permissions import SoloAdministrador

# Create your views here.
class RegistroUsuarioApiView(generics.CreateAPIView):
    permission_classes = [permissions.IsAuthenticated, SoloAdministrador]
    def post(self, request: request.Request):
        serializador = RegistroUsuarioSerializer(data = request.data)

        if serializador.is_valid():
            nuevo_usuario = UsuarioModel(**serializador.validated_data)
            nuevo_usuario.set_password(serializador.validated_data.get('password'))

            nuevo_usuario.save()
            return response.Response(data={
                'message': 'Usuario creado exitosamente'
            }, status=status.HTTP_201_CREATED)
        else:
            return response.Response(data={
                'message': 'Error al registrar al usuario',
                'content': serializador.errors
            }, status=status.HTTP_400_BAD_REQUEST)
            
class RegistroPacienteApiView(generics.CreateAPIView):
    permission_classes = [permissions.IsAuthenticated, SoloAdministrador]
    def post(self, request: request.Request):
        serializador = RegistroPacienteSerializer(data = request.data)

        if serializador.is_valid():
            nuevo_paciente = PacienteModel(**serializador.validated_data)
            nuevo_paciente.save()
            return response.Response(data={
                'message': 'Paciente creado exitosamente'
            }, status=status.HTTP_201_CREATED)
        else:
            return response.Response(data={
                'message': 'Error al registrar al paciente',
                'content': serializador.errors
            }, status=status.HTTP_400_BAD_REQUEST)   
                     
class RegistroCitaApiView(generics.CreateAPIView):
    permission_classes = [permissions.IsAuthenticated, SoloAdministrador]
    def post(self, request: request.Request):
        serializador = RegistroCitaSerializer(data = request.data)

        if serializador.is_valid():
            nueva_cita = CitaModel(**serializador.validated_data)
            nueva_cita.save()
            return response.Response(data={
                'message': 'Cita creado exitosamente'
            }, status=status.HTTP_201_CREATED)
        else:
            return response.Response(data={
                'message': 'Error al registrar la cita',
                'content': serializador.errors
            }, status=status.HTTP_400_BAD_REQUEST)

class PerfilUsuarioApiView(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request: request.Request):
        print(request.user)
        print(request.auth)
        usuario_encontrado = MostrarUsuarioSerializer(instance= request.user)

        return response.Response(data={
            'content': usuario_encontrado.data
        })

class UnPacienteApiView(generics.RetrieveUpdateAPIView):
    def get(self, request, id):
        # SELECT * FROM pacientes WHERE id = ...;
        resultado = PacienteModel.objects.filter(id = id).first()
        if resultado is None:
            return response.Response(data={
                'message': 'El paciente no existe'
            }, status= status.HTTP_404_NOT_FOUND)
        
        serializador = MostrarPacienteSerializer(instance=resultado)
        
        return response.Response(data={
            'message': serializador.data
        }, status=status.HTTP_200_OK)
    
    def put(self, request: request.Request, id):
        resultado = PacienteModel.objects.filter(id = id).first()
        if resultado is None:
            return response.Response(data={
                'message': 'El paciente no existe'
            }, status= status.HTTP_404_NOT_FOUND)
        
        data_serializada = MostrarPacienteSerializer(data= request.data)

        if data_serializada.is_valid():
            resultado.ocupacion_actual = data_serializada.data.get('ocupacion_actual')
            resultado.fecha_ingreso = data_serializada.data.get('fecha_ingreso')
            #, antecedentes_personales, padre_vive, madre_vive, enfermedad_ocupacional, accidente_ocupacional, accidente_particular, cirugia ,correo, telefono ')
            resultado.save()

            return response.Response(data={
                'message': 'Paciente actualizado exitosamente'
            })

        else:
            return response.Response(data={
                'message': 'Error al actualizar el paciente',
                'content': data_serializada.errors
            })


class UnaCitaApiView(generics.RetrieveUpdateAPIView):
    def get(self, request, id):
        # SELECT * FROM categorias WHERE id = ...;
        resultado = CitaModel.objects.filter(id = id).first()
        if resultado is None:
            return response.Response(data={
                'message': 'La cita no existe'
            }, status= status.HTTP_404_NOT_FOUND)
        
        serializador = MostrarCitaSerializer(instance=resultado)
        
        return response.Response(data={
            'message': serializador.data
        }, status=status.HTTP_200_OK)
    
    def put(self, request: request.Request, id):
        resultado = CitaModel.objects.filter(id = id).first()
        if resultado is None:
            return response.Response(data={
                'message': 'La cita no existe'
            }, status= status.HTTP_404_NOT_FOUND)
        
        data_serializada = MostrarCitaSerializer(data= request.data)

        if data_serializada.is_valid():
            resultado.fecha = data_serializada.data.get('fecha')
            resultado.tipo_atencion = data_serializada.data.get('tipo_atencion')
            resultado.usuarioId = data_serializada.data.get('usuarioId')
            resultado.pacienteId = data_serializada.data.get('pacienteId')
            resultado.save()

            return response.Response(data={
                'message': 'cita actualizada exitosamente'
            })

        else:
            return response.Response(data={
                'message': 'Error al actualizar la cita',
                'content': data_serializada.errors
            })
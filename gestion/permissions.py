from rest_framework.permissions import BasePermission

class SoloAdministrador(BasePermission):
    message = 'Solo los Administradores pueden acceder a esta ruta'
    
    def has_permission(self, request, view):
        # request.user > devuelve el usuario identificado
        tipoUsuario = request.user.tipoUsuario
        if tipoUsuario == 'ADMIN':
            return True
        
        else: 
            return False
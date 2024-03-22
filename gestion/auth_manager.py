# Para crear superusuario por consola

from django.contrib.auth.models import BaseUserManager

class UsuarioManager(BaseUserManager):
    def create_superuser(self, correo, primer_nombre,segundo_nombre, apellido_paterno, apellido_materno, password):
        if not correo:
            raise ValueError('El usuario debe tener un correo')
        
        correo_nomalizado = self.normalize_email(correo)
        nuevo_usuario = self.model(correo=correo_nomalizado, primer_nombre=primer_nombre, segundo_nombre=segundo_nombre, apellido_paterno=apellido_paterno, apellido_materno=apellido_materno)
        nuevo_usuario.set_password(password)

        nuevo_usuario.is_superuser=True
        nuevo_usuario.is_staff = True

        nuevo_usuario.save()
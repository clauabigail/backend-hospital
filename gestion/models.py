from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .auth_manager import UsuarioManager

# Create your models here.

class UsuarioModel(AbstractBaseUser, PermissionsMixin):
    id = models.AutoField(primary_key=True, null = False)
    registro= models.CharField(max_length=10, unique = True)
    dni = models.CharField(max_length=10, unique = True)
    apellido_paterno = models.CharField(max_length=100, null=False)
    apellido_materno = models.CharField(max_length=100, null=False)
    primer_nombre = models.CharField(max_length=100, null=False)
    segundo_nombre = models.CharField(max_length = 50)
    profesion = models.CharField(max_length=100, null=False)
    colegiatura = models.CharField(max_length=100, unique=True)
    correo = models.EmailField(max_length=100, unique=True, null=False)
    password = models.CharField(max_length=100, null = False)
    telefono = models.CharField(max_length=100, unique=True)
    direccion = models.CharField(max_length=100, unique=True)
         
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    tipoUsuario = models.CharField(max_length=100, choices= [('ADMIN', 'ADMIN'), ('TRABAJADOR', 'TRABAJADOR')], default='ADMIN', db_column='tipo_usuario')
    
    createdAt = models.DateTimeField(auto_now_add=True, db_column='created_at')

    # si queremos ingresar al panel administrativo que atributo utilizara para pedirle al usuario
    USERNAME_FIELD = 'correo'
    # cuando queremos crear un superusuario por la terminal que atributos nos debe de solicitar
    REQUIRED_FIELDS = ['primer_nombre', 'segundo_nombre', 'apellido_paterno', 'apellido_materno']
    
    objects = UsuarioManager()
     
    class Meta:
        db_table = 'usuarios'
        
                
class PacienteModel(models.Model):
    id = models.AutoField(primary_key=True, null = False)
    registro = models.CharField(max_length=10, unique = True)
    dni = models.CharField(max_length=10, unique = True, null= False)
    empresa = models.CharField(max_length=50)
    apellido_paterno = models.CharField(max_length=100, null=False)
    apellido_materno = models.CharField(max_length=100, null=False)
    primer_nombre = models.CharField(max_length=50, null=False)
    segundo_nombre = models.CharField(max_length = 50)
    sexo = models.CharField(max_length=50, choices= [('FEMENINO', 'FEMENINO'), ('MASCULINO', 'MASCULINO')], default='MASCULINO', db_column='sexo', null = False)
    lugar_nacimiento = models.CharField(max_length=100, null=False)
    fecha_nacimiento = models.DateTimeField(db_column='fecha_nacimiento')
    estado_civil =models.CharField(max_length=50, choices= [('SOLTERO', 'SOLTERO'), ('CASADO', 'CASADO'), ('CONVIVIENTE', 'CONVIVIENTE'), ('VIUDO', 'VIUDO'), ('DIVORCIADO','DIVORCIADO')], default='SOLTERO', db_column='estado_civil')
    ocupacion_actual = models.CharField(max_length=100)
    grado_instruccion = models.CharField(max_length=50, choices= [('TECNICO', 'TECNICO'), ('UNIVERSITARIO', 'UNIVERSITARIO')], default = 'TECNICO')
    antecedentes_personales = models.BooleanField(default=False)
    padre_vive = models.BooleanField(default=True)
    madre_vive= models.BooleanField(default=True)
    enfermedad_ocupacional = models.TextField(default='NINGUNO')
    hermanos_vivos = models.IntegerField()
    fecha_ingreso = models.DateTimeField(db_column='fecha_ingreso')
    accidente_ocupacional = models.TextField(default='NINGUNO')
    accidente_particular = models.TextField(default='NINGUNO')
    cirugia = models.BooleanField(default=False)
    grupo_sanguineo = models.CharField(max_length=50, choices= [('O', 'O'), ('A', 'A'), ('B', 'B'), ('AB', 'AB')], default='O', db_column='grupo_sanguineo')
    rh = models.CharField(max_length=50, choices= [('+', '+'), ('-', '-')], default='+', db_column='r_h')
    correo = models.EmailField(max_length=100, unique=True, null=False)
    telefono = models.CharField(max_length=100)
            
    class Meta:
        db_table = 'pacientes'
        

class DireccionModel(models.Model):
    id= models.AutoField(primary_key= True, null=False)
    departamento = models.CharField(max_length=20, null=False)
    provincia = models.CharField(max_length=20, null=False)
    distrito = models.CharField(max_length=30, null=False)
    calle = models.CharField(max_length=50, null=False)
    numero = models.CharField(max_length=8, null=False)
    pacienteId = models.ForeignKey(to = PacienteModel , on_delete=models.CASCADE, db_column='paciente_id', default = '1')
        
    class Meta:
        db_table = 'direcciones'   
    
        
class CitaModel(models.Model):
    id = models.AutoField(primary_key=True, null = False)
    fecha = models.DateField(db_column= 'fecha_cita')
    tipo_atencion = models.CharField(max_length=50, choices= [('PREOCUPACIONAL', 'PREOCUPACIONAL'), ('PERIODICO', 'PERIODICO'), ('RETIRO', 'RETIRO'),('REUBICACION', 'REUBICACION')], default = 'PERIODICO', db_column= 'tipo_cita')
    usuarioId = models.ForeignKey(to= UsuarioModel, on_delete=models.CASCADE, db_column='usuario_id')
    pacienteId = models.ForeignKey(to= PacienteModel, on_delete=models.CASCADE, db_column='paciente_id')
        
    class Meta:
        db_table = 'citas'

class DetalleCitaModel(models.Model):
    id = models.AutoField(primary_key=True, null = False)
    atendido= models.BooleanField(default='True')
    cita = models.OneToOneField(CitaModel, on_delete=models.CASCADE)
    electrocardio = models.TextField()
    diagnostico = models.TextField()
    audiometria = models.TextField()
    examOftalmologico = models.TextField()
    rayosX = models.TextField()
            
    class Meta:
        db_table = 'detalle_citas'       
        
class FactorRiesgoModel(models.Model):
    id = models.AutoField(primary_key=True, null = False)
    ruido = models.BooleanField(default=False)
    polvo = models.BooleanField(default=False)
    cancerigenos = models.BooleanField(default=False)
    metalesPesados = models.BooleanField(default=False)
    vibSegmentaria = models.BooleanField(default=False)
    mutagenicos = models.BooleanField(default=False)
    biologicos = models.BooleanField(default=False)
    solventes = models.BooleanField(default=False)
    temperaturas = models.BooleanField(default=False)
    cargas = models.BooleanField(default=False)
    movRespiratorio = models.BooleanField(default=False)
    posturas = models.BooleanField(default=False)
    turnos = models.BooleanField(default=False)
    pvd = models.BooleanField(default=False)
    otros = models.TextField()
    detalle_cita = models.OneToOneField(DetalleCitaModel, on_delete=models.CASCADE)
    
    class Meta:
        db_table= 'factores_riesgo'   
        
class LaboratorioModel(models.Model):
    id = models.AutoField(primary_key= True, null= False)
    fecha_lab = models.DateField(null= False, db_column = 'fecha_lab')
    hemoglobina = models.TextField()
    CT =  models.FloatField()
    HDL = models.FloatField()
    LDL = models.FloatField()
    trigliceridos = models.FloatField()
    glucosa = models.FloatField()
    creatinina = models.FloatField()
    riesgo_cv = models.BooleanField(default = False)
    detalle_cita = models.OneToOneField(DetalleCitaModel, on_delete=models.CASCADE)
    
    class Meta:
        db_table = 'ex_laboratorios'  
        
class EspirometriaModel(models.Model):
    id = models.AutoField(primary_key= True, null = False)
    fecha_espiro = models.DateField(null= False, db_column = 'fecha_espiro')
    interpretacion = models.TextField()
    fvc = models.FloatField()
    porcentaje_fvc = models.FloatField()
    fev1 = models.FloatField()
    porcentaje_fev1 = models.FloatField()
    tiffeneau = models.FloatField()
    broncodi = models.TextField()
    detalle_cita = models.OneToOneField(DetalleCitaModel, on_delete=models.CASCADE)
    
    class Meta:
        db_table= 'espirometrias'     
                      
        


        
        
        
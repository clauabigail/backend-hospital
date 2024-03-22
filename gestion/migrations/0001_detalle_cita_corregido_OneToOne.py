# Generated by Django 5.0.3 on 2024-03-22 05:18

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='PacienteModel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('registro', models.CharField(max_length=10, unique=True)),
                ('empresa', models.CharField(max_length=50)),
                ('apellido_paterno', models.CharField(max_length=100)),
                ('apellido_materno', models.CharField(max_length=100)),
                ('primer_nombre', models.CharField(max_length=50)),
                ('segundo_nombre', models.CharField(max_length=50)),
                ('sexo', models.CharField(choices=[('FEMENINO', 'FEMENINO'), ('MASCULINO', 'MASCULINO')], db_column='sexo', default='MASCULINO', max_length=50)),
                ('lugar_nacimiento', models.CharField(max_length=100)),
                ('fecha_nacimiento', models.DateTimeField(db_column='fecha_nacimiento')),
                ('estado_civil', models.CharField(choices=[('SOLTERO', 'SOLTERO'), ('CASADO', 'CASADO'), ('CONVIVIENTE', 'CONVIVIENTE'), ('VIUDO', 'VIUDO'), ('DIVORCIADO', 'DIVORCIADO')], db_column='estado_civil', default='SOLTERO', max_length=50)),
                ('dni', models.CharField(max_length=10, unique=True)),
                ('ocupacion_actual', models.CharField(max_length=100)),
                ('grado_instruccion', models.CharField(choices=[('TECNICO', 'TECNICO'), ('UNIVERSITARIO', 'UNIVERSITARIO')], default='TECNICO', max_length=50)),
                ('antecedentes_personales', models.BooleanField(default=False)),
                ('padre_vive', models.BooleanField(default=True)),
                ('madre_vive', models.BooleanField(default=True)),
                ('enfermedad_ocupacional', models.TextField()),
                ('hermanos_vivos', models.IntegerField()),
                ('fecha_ingreso', models.DateTimeField(db_column='fecha_ingreso')),
                ('accidente_ocupacional', models.TextField()),
                ('accidente_particular', models.TextField()),
                ('cirugia', models.BooleanField(default=False)),
                ('grupo_sanguineo', models.CharField(choices=[('O', 'O'), ('A', 'A'), ('B', 'B'), ('AB', 'AB')], db_column='grupo_sanguineo', default='O', max_length=50)),
                ('rh', models.CharField(choices=[('+', '+'), ('-', '-')], db_column='r_h', default='+', max_length=50)),
                ('correo', models.EmailField(max_length=100, unique=True)),
                ('telefono', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'pacientes',
            },
        ),
        migrations.CreateModel(
            name='UsuarioModel',
            fields=[
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('registro', models.CharField(max_length=10, unique=True)),
                ('dni', models.CharField(max_length=10, unique=True)),
                ('apellido_paterno', models.CharField(max_length=100)),
                ('apellido_materno', models.CharField(max_length=100)),
                ('primer_nombre', models.CharField(max_length=100)),
                ('segundo_nombre', models.CharField(max_length=50)),
                ('profesion', models.CharField(max_length=100)),
                ('colegiatura', models.CharField(max_length=100, unique=True)),
                ('correo', models.EmailField(max_length=100, unique=True)),
                ('password', models.CharField(max_length=100)),
                ('telefono', models.CharField(max_length=100, unique=True)),
                ('direccion', models.CharField(max_length=100, unique=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('tipoUsuario', models.CharField(choices=[('ADMIN', 'ADMIN'), ('TRABAJADOR', 'TRABAJADOR')], db_column='tipo_usuario', default='ADMIN', max_length=100)),
                ('createdAt', models.DateTimeField(auto_now_add=True, db_column='created_at')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'db_table': 'usuarios',
            },
        ),
        migrations.CreateModel(
            name='CitaModel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('fecha', models.DateField(db_column='fecha_cita')),
                ('tipo_atencion', models.CharField(choices=[('PREOCUPACIONAL', 'PREOCUPACIONAL'), ('PERIODICO', 'PERIODICO'), ('RETIRO', 'RETIRO'), ('REUBICACION', 'REUBICACION')], db_column='tipo_cita', default='PERIODICO', max_length=50)),
                ('usuarioId', models.ForeignKey(db_column='usuario_id', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('pacienteId', models.ForeignKey(db_column='paciente_id', on_delete=django.db.models.deletion.CASCADE, to='gestion.pacientemodel')),
            ],
            options={
                'db_table': 'citas',
            },
        ),
        migrations.CreateModel(
            name='DetalleCitaModel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('atendido', models.BooleanField(default='True')),
                ('electrocardio', models.TextField()),
                ('diagnostico', models.TextField()),
                ('audiometria', models.TextField()),
                ('examOftalmologico', models.TextField()),
                ('rayosX', models.TextField()),
                ('cita', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='gestion.citamodel')),
            ],
            options={
                'db_table': 'detalle_citas',
            },
        ),
        migrations.CreateModel(
            name='EspirometriaModel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('fecha_espiro', models.DateField(db_column='fecha_espiro')),
                ('interpretacion', models.TextField()),
                ('fvc', models.FloatField()),
                ('porcentaje_fvc', models.FloatField()),
                ('fev1', models.FloatField()),
                ('porcentaje_fev1', models.FloatField()),
                ('tiffeneau', models.FloatField()),
                ('broncodi', models.TextField()),
                ('detalle_cita', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='gestion.detallecitamodel')),
            ],
            options={
                'db_table': 'espirometrias',
            },
        ),
        migrations.CreateModel(
            name='FactorRiesgoModel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('ruido', models.BooleanField(default=False)),
                ('polvo', models.BooleanField(default=False)),
                ('cancerigenos', models.BooleanField(default=False)),
                ('metalesPesados', models.BooleanField(default=False)),
                ('vibSegmentaria', models.BooleanField(default=False)),
                ('mutagenicos', models.BooleanField(default=False)),
                ('biologicos', models.BooleanField(default=False)),
                ('solventes', models.BooleanField(default=False)),
                ('temperaturas', models.BooleanField(default=False)),
                ('cargas', models.BooleanField(default=False)),
                ('movRespiratorio', models.BooleanField(default=False)),
                ('posturas', models.BooleanField(default=False)),
                ('turnos', models.BooleanField(default=False)),
                ('pvd', models.BooleanField(default=False)),
                ('otros', models.TextField()),
                ('detalle_cita', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='gestion.detallecitamodel')),
            ],
            options={
                'db_table': 'factores_riesgo',
            },
        ),
        migrations.CreateModel(
            name='LaboratorioModel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('fecha_lab', models.DateField(db_column='fecha_lab')),
                ('hemoglobina', models.TextField()),
                ('CT', models.FloatField()),
                ('HDL', models.FloatField()),
                ('LDL', models.FloatField()),
                ('trigliceridos', models.FloatField()),
                ('glucosa', models.FloatField()),
                ('creatinina', models.FloatField()),
                ('riesgo_cv', models.BooleanField(default=False)),
                ('detalle_cita', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='gestion.detallecitamodel')),
            ],
            options={
                'db_table': 'ex_laboratorios',
            },
        ),
        migrations.CreateModel(
            name='DireccionModel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('departamento', models.CharField(max_length=20)),
                ('provincia', models.CharField(max_length=20)),
                ('distrito', models.CharField(max_length=30)),
                ('calle', models.CharField(max_length=50)),
                ('numero', models.CharField(max_length=8)),
                ('pacienteId', models.ForeignKey(db_column='paciente_id', default='1', on_delete=django.db.models.deletion.CASCADE, to='gestion.pacientemodel')),
            ],
            options={
                'db_table': 'direcciones',
            },
        ),
    ]

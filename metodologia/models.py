# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

class GrupoVigilado(models.Model):
    TIPO_GRUPO = (
        ('objetivo','objetivo'),
        ('subjetivo','subjetivo'),
    )
    id = models.BigAutoField(primary_key=True)
    vigilancia = models.CharField(max_length=9,
                              choices=TIPO_GRUPO,
                              default='objetivo')
    nombre = models.CharField(max_length=128)

    class Meta:
        db_table = 'grupo_vigilado'

    def __str__(self):
        return self.vigilancia + '-' + self.nombre


class Vigilado(models.Model):
    MODOS = (
        ('aereo','aereo'),
        ('carretero','carretero'),
        ('ferreo','ferreo'),
        ('terminales','terminales'),
    )
    VIGILANCIA = (
        ('integral','integral'),
        ('objetivo','objetivo'),
        ('subjetivo','subjetivo'),
    )
    id = models.BigAutoField(primary_key=True)
    modo = models.CharField(max_length=10,
                              choices=MODOS,
                              default='aereo')
    nombre = models.CharField(max_length=128)
    ciudad = models.CharField(max_length=64)
    departamento = models.CharField(max_length=64)
    vigilancia = models.CharField(max_length=9,
                              choices=VIGILANCIA,
                              default='integral')
    nit = models.BigIntegerField()    
    grupo = models.ForeignKey('GrupoVigilado', models.DO_NOTHING, blank=True, null=True)
    pertenece_a = models.ForeignKey('Vigilado', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        db_table = 'vigilado'

    def __str__(self):
        return self.modo + '-' + self.nombre

class GrupoVigiladoVigilado(models.Model):
    id = models.BigAutoField(primary_key=True)
    grupo_vigilado = models.ForeignKey('GrupoVigilado', models.DO_NOTHING, blank=True, null=True)
    vigilado = models.ForeignKey('Vigilado', models.DO_NOTHING, blank=True, null=True)
    
    class Meta:
        db_table = 'grupo_vigilado_vigilado'

    def __str__(self):
        return str(self.id)



class GrupoObjetivo(models.Model):
    MODOS = (
        ('aereo','aereo'),
        ('carretero','carretero'),
        ('ferreo','ferreo'),
        ('terminales','terminales'),
    )
    id = models.BigAutoField(primary_key=True)
    modo = models.CharField(max_length=10,
                              choices=MODOS,
                              default='aereo')
    nombre = models.CharField(max_length=128)

    class Meta:
        db_table = 'grupo_objetivo'

    def __str__(self):
        return self.modo + '-' + self.nombre

class VariableObjetivo(models.Model):
    IMPACTO = (
               (0, 'No'),
               (1, 'Si'),
    )
    PESO = (
               (0, '0'),
               (1, '1'),
               (2, '2'),
               (3, '3'),
    )
    
    id = models.BigAutoField(primary_key=True)
    codigo = models.CharField(max_length=5)
    nombre = models.CharField(max_length=512)
    descripcion = models.CharField(max_length=512, blank=True, null=True)
    formula = models.CharField(max_length=255, blank=True, null=True)
    rango = models.CharField(max_length=255, blank=True, null=True)
    unidad = models.CharField(max_length=255, blank=True, null=True)
    c = models.IntegerField(default=0, choices=IMPACTO)
    s = models.IntegerField(default=0, choices=IMPACTO)
    a = models.IntegerField(default=0, choices=IMPACTO)
    imp_c = models.IntegerField(default=0, choices=PESO)
    imp_s = models.IntegerField(default=0, choices=PESO)
    imp_a = models.IntegerField(default=0, choices=PESO)
    grupo = models.ForeignKey('GrupoObjetivo', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        db_table = 'variable_objetivo'

    def __str__(self):
        return self.codigo + '-' + self.nombre

class GrupoVigiladoVariableObjetivo(models.Model):
    OBLIGATORIA = (
        ('S','S'),
        ('N','N'),
    )
    id = models.BigAutoField(primary_key=True)
    obligatoria = models.CharField(max_length=1,
                              choices=OBLIGATORIA,
                              default='N')
    grupo_vigilado = models.ForeignKey('GrupoVigilado', models.DO_NOTHING, blank=True, null=True)
    variable_subjetivo = models.ForeignKey('VariableObjetivo', models.DO_NOTHING, blank=True, null=True)
    
    class Meta:
        db_table = 'grupo_vigilado_variable_objetivo'

    def __str__(self):
        return str(self.id)


class FactorSubjetivo(models.Model):
    id = models.BigAutoField(primary_key=True)
    nombre = models.CharField(max_length=128)

    class Meta:
        db_table = 'factor_subjetivo'
    
    def __str__(self):
        return self.nombre

class GrupoVariableSubjetivo(models.Model):
    id = models.BigAutoField(primary_key=True)
    nombre = models.CharField(max_length=128)
    factor = models.ForeignKey('FactorSubjetivo', models.DO_NOTHING, blank=True, null=True)
    
    class Meta:
        db_table = 'grupo_variable_subjetivo'

    def __str__(self):
        return self.nombre

class VariableSubjetivo(models.Model):
    id = models.BigAutoField(primary_key=True)
    codigo = models.CharField(max_length=7)
    nombre = models.CharField(max_length=512)
    formula = models.CharField(max_length=255, blank=True, null=True)
    rango = models.CharField(max_length=512, blank=True, null=True)
    grupo_variable_subjetivo = models.ForeignKey('GrupoVariableSubjetivo', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        db_table = 'variable_subjetivo'

    def __str__(self):
        return self.codigo + '-' + self.nombre

class GrupoVigiladoVariableSubjetivo(models.Model):
    OBLIGATORIA = (
        ('S','S'),
        ('N','N'),
    )
    id = models.BigAutoField(primary_key=True)
    obligatoria = models.CharField(max_length=1,
                              choices=OBLIGATORIA,
                              default='N')
    grupo_vigilado = models.ForeignKey('GrupoVigilado', models.DO_NOTHING, blank=True, null=True)
    variable_subjetivo = models.ForeignKey('VariableSubjetivo', models.DO_NOTHING, blank=True, null=True)
    
    class Meta:
        db_table = 'grupo_vigilado_variable_subjetivo'

    def __str__(self):
        return str(self.id)
        
class GrupoVigiladoFactorSubjetivo(models.Model):
    id = models.BigAutoField(primary_key=True)
    ponderacion = models.IntegerField(blank=True, null=True)
    grupo_vigilado = models.ForeignKey('GrupoVigilado', models.DO_NOTHING, blank=True, null=True)
    factor_subjetivo = models.ForeignKey('FactorSubjetivo', models.DO_NOTHING, blank=True, null=True)
    
    class Meta:
        db_table = 'grupo_vigilado_factor_subjetivo'

    def __str__(self):
        return str(self.id)
        
class GrupoVigiladoVariableObjetivo(models.Model):
    id = models.BigAutoField(primary_key=True)
    grupo_vigilado = models.ForeignKey('GrupoVigilado', models.DO_NOTHING, blank=True, null=True)
    variable_objetivo = models.ForeignKey('VariableObjetivo', models.DO_NOTHING, blank=True, null=True)
    
    class Meta:
        db_table = 'grupo_vigilado_variable_objetivo'

    def __str__(self):
        return str(self.id)

class Indicador(models.Model):
    INDICADORES = (
        ('estrategico','estrategico'),
        ('tactico','tactico'),
        ('subjetivo','subjetivo'),
        ('factor general','factor general'),
        ('factor obligatorio','factor obligatorio'),
        ('factor riesgo','factor riesgo'),
    )
    TIPO_GRUPO = (
        ('objetivo','objetivo'),
        ('subjetivo','subjetivo'),
    )
    id = models.BigAutoField(primary_key=True)
    vigilancia = models.CharField(max_length=9,
                              choices=TIPO_GRUPO,
                              default='objetivo')
    tipo = models.CharField(max_length=20,
                              choices=INDICADORES,
                              default='tactico')
                              
    nombre = models.CharField(max_length=128)
    valor = models.FloatField()
    vigilado = models.ForeignKey('Vigilado', models.DO_NOTHING, blank=True, null=True)
    tiempo = models.ForeignKey('TiempoMedida', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        db_table = 'indicador'

    def __str__(self):
        return self.nombre
        

class MedidaObjetivo(models.Model):
    id = models.BigAutoField(primary_key=True)
    categoria = models.CharField(max_length=24)
    valor = models.IntegerField()
    ingresado = models.CharField(max_length=24, null=True, blank=True)
    evaluado = models.CharField(max_length=24, null=True, blank=True)
    variable_objetivo = models.ForeignKey('VariableObjetivo', models.DO_NOTHING, blank=True, null=True)
    vigilado = models.ForeignKey('Vigilado', models.DO_NOTHING, blank=True, null=True)
    tiempo = models.ForeignKey('TiempoMedida', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        db_table = 'medida_objetivo'

    def __str__(self):
        return self.categoria


class MedidaSubjetivo(models.Model):
    MEDIDA_SUBJETIVO = (
        ('fuerte','fuerte'),
        ('avanzado','avanzado'),
        ('intermedio','intermedio'),
        ('debil','debil'),
        ('inadecuado','inadecuado'),
        ('no existe','no existe'),
    )
    id = models.BigAutoField(primary_key=True)
    categoria = models.CharField(max_length=10,
                              choices=MEDIDA_SUBJETIVO,
                              default='no existe')
    valor = models.IntegerField()
    variable_subjetivo = models.ForeignKey('VariableSubjetivo', models.DO_NOTHING, blank=True, null=True)
    vigilado = models.ForeignKey('Vigilado', models.DO_NOTHING, blank=True, null=True)
    tiempo = models.ForeignKey('TiempoMedida', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        db_table = 'medida_subjetivo'

    def __str__(self):
        return self.categoria

class TiempoMedida(models.Model):
    ORIGEN = (
        ('vigilancia','vigilancia'),
        ('inspeccion','inspeccion'),
        ('control','control'),
    )

    id = models.BigAutoField(primary_key=True)
    fecha = models.DateField(auto_now=True)
    origen = models.CharField(max_length=10,
                              choices=ORIGEN,
                              default='VIGILANCIA')
    flag_calculo = models.BooleanField(default=False)

    class Meta:
        db_table = 'tiempo_medida'

    def __str__(self):
        return self.origen


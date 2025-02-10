from django.db import models



class Oficina(models.Model):

    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    ubicacion = models.TextField()
    responsable = models.CharField(max_length=100)
    capacidad = models.IntegerField()
    estado = models.CharField(max_length=50, choices=[('Disponible', 'Disponible'), ('En remodelación', 'En remodelación'),('Ocupada', 'Ocupada')])





class Contratista(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    empresa = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)
    correo = models.EmailField()
    especialidad = models.CharField(max_length=100)
    fotografia=models.FileField(upload_to='contrato',null=True,blank=True )







class Reforma(models.Model):

    id = models.AutoField(primary_key=True)
    oficina = models.ForeignKey(Oficina, on_delete=models.CASCADE)
    contratista = models.ForeignKey(Contratista, on_delete=models.CASCADE)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField(null=True, blank=True)
    presupuesto = models.DecimalField(max_digits=10, decimal_places=2)
    descripcion = models.TextField()
    reforma = models.CharField(max_length=50, choices=[('Pendiente', 'Pendiente'), ('En Progreso', 'En Progreso'),('Finalizado', 'Finalizado')])






class Suministro(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    cantidad = models.IntegerField()
    costo_unitario = models.DecimalField(max_digits=10, decimal_places=2)
    evidencias=models.FileField(upload_to='sumini',null=True,blank=True )






class ReformaSuministro(models.Model):
    reforma = models.ForeignKey(Reforma, on_delete=models.CASCADE)
    suministro = models.ForeignKey(Suministro, on_delete=models.CASCADE)
    cantidad_usada = models.IntegerField()


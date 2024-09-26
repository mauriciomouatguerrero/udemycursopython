from django.db import models

# Create your models here.

from applications.departamento.models import Departamento

class Habilidades(models.Model):
    habilidad = models.CharField('Habilidad', max_length=50)

    class Meta:
        verbose_name = 'Habilidad'
        verbose_name_plural = 'Habilidad Empleados'

    def __str__(self):
        return str(self.id) + '-' + self.habilidad
    

class Empleado(models.Model):
    JOB_CHOICES = (
        (0, 'CONTADOR'),
        (1, 'ADMINISTRADOR'),
        (2, 'ECONOMISTA'),
        (3, 'OTRO'),
    )

    first_name = models.CharField('Nombres', max_length=60)
    last_name = models.CharField('Apellidos', max_length=60)
    job = models.IntegerField('Trabajo', choices=JOB_CHOICES)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='empleado', blank=True, null=True)
    habilidades = models.ManyToManyField(Habilidades)

    def __str__(self):
        return str(self.id) + '-' + self.first_name + ' ' + self.last_name
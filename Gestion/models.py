
from django.db import models

# Create your models here.

class Alumno(models.Model):
    ApellidoPaterno = models.CharField(max_length=15)
    ApellidoMaterno = models.CharField(max_length=15)
    Nombres = models.CharField(max_length=15)
    cedula = models.CharField(max_length=8)
    FechaNacimiento = models.DateField()
    SEXOS = (('F', 'Femenino'),('M', 'Masculino')) 
    Sexo = models.CharField(max_length=1, choices=SEXOS, default='M')

    def NombreCompleto(self):
        cadena = "{0} {1}, {2} "
        return cadena.format(self.ApellidoPaterno, self.ApellidoMaterno, self.Nombres)

    def toJSON(self):
        item = model_to_dict(self)
        return item

    def __str__(self):
        return self.NombreCompleto()

class Curso(models.Model):

    Nombre = models.CharField(max_length=60)
    Creditos = models.PositiveSmallIntegerField()
    Estado = models.BooleanField(default=True)

    def __str__(self):
        return " {0} ({1}) ".format(self.Nombre, self.Creditos)


class Matricula(models.Model):
    Alumno = models.ForeignKey(Alumno, null=False, on_delete=models.CASCADE)
    Curso = models.ForeignKey(Curso, null=False, on_delete=models.CASCADE)  
    FechaMatricula = models.DateTimeField(auto_now_add=True)  

    def __str__(self):
        return " {0} => {1} ".format(self.Alumno, self.Curso.Nombre)
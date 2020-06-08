from django.forms import ModelForm
from Gestion.models import Alumno, Curso, Matricula


class alumnoForm(ModelForm):
    
    class Meta:
        model = Alumno
        fields = (
            "ApellidoPaterno",
            "ApellidoMaterno",
            "Nombres",
            "cedula",
            "FechaNacimiento",
            "Sexo", 
        )

class cursoForm(ModelForm):
    
    class Meta:
        model = Curso
        fields = (
            "Nombre",
            "Creditos",
            "Estado"
        )

class matriculaForm(ModelForm):
    
    class Meta:
        model = Matricula
        fields = (
            "Alumno",
            "Curso"
        )


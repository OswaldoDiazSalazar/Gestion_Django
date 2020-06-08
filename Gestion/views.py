from Gestion.models import Alumno, Curso, Matricula
from Gestion.forms import alumnoForm, cursoForm, matriculaForm
from django.views.generic import CreateView, UpdateView, ListView, DeleteView
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy


# Create your views here.


class AlumnoListView(ListView):
    model = Alumno
    template_name = 'alumno/listado.html'

    # @method_decorator(csrf_exempt)
    # def dispatch(self, request, *args, **kwargs):
    #     return super().dispatch(request, *args, **kwargs)

    # def post(self, request, *args, **kwargs):
    #     data = {}
    #     try:
    #         data = Alumno.objects.get(pk=request.POST['id']).toJSON()
    #     except Exception as e:
    #         data['error'] = str(e)
    #     return JsonResponse(data)

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['title'] = 'Listado de Alumnos'
    #     context['create_url'] = reverse_lazy('createalumno')
    #     context['list_url'] = reverse_lazy('listaralumno')
    #     context['entity'] = 'Alumno'
    #     return context    

class Createalumno(CreateView):
    model = Alumno
    form_class = alumnoForm
    template_name = 'createAlumno.html'
    success_url = '/gestion/listaralumno'

class Updatealumno(UpdateView):
    model = Alumno
    form_class = alumnoForm
    template_name = 'alumno/create.html'
    success_url = '/gestion/listaralumno' 

class Deletealumno(DeleteView):
    model = Alumno
    template_name = 'alumno/delete.html'
    success_url = '/gestion/listaralumno' 



class MatriculaListView(ListView):
    model = Matricula
    template_name = 'matricula/listado.html'

class Creatematricula(CreateView):
    model = Matricula
    form_class = matriculaForm
    template_name = 'matricula/create.html'
    success_url = '/gestion/listarmatricula'

class Updatematricula(UpdateView):
    model = Matricula
    form_class = matriculaForm
    template_name = 'matricula/create.html'
    success_url = '/gestion/listarmatricula'

class Deletematricula(DeleteView):
    model = Matricula
    template_name = 'matricula/delete.html'
    success_url = '/gestion/listarmatricula' 


class CursoListView(ListView):
    model = Curso
    template_name = 'curso/listado.html'


class Createcurso(CreateView):
    model = Curso
    form_class = cursoForm
    template_name = 'curso/create.html'
    success_url = '/gestion/listarcurso'

class Updatecurso(UpdateView):
    model = Curso
    form_class = cursoForm
    template_name = 'curso/create.html'
    success_url = '/gestion/listarcurso' 

class Deletecurso(DeleteView):
    model = Curso
    template_name = 'curso/delete.html'
    success_url = '/gestion/listarcurso'     

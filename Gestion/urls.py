
from django.urls import path
from Gestion.views import *

urlpatterns = [
    path('', MatriculaListView.as_view(), name='home'),

    path('listarmatricula/', MatriculaListView.as_view(), name = 'listarmatricula'),
    path('listaralumno/', AlumnoListView.as_view(), name = 'listaralumno'),
    path('listarcurso/', CursoListView.as_view(), name = 'listarcurso'),
    
    path('creatematricula/', Creatematricula.as_view(), name = 'crearmatricula'),
    path('createalumno/', Createalumno.as_view(), name = 'crearalumno'),
    path('createcurso/', Createcurso.as_view(), name = 'crearcurso'),

    path('updatematricula/<pk>', Updatematricula.as_view()),   
    path('updatealumno/<pk>', Updatealumno.as_view()),
    path('updatecurso/<pk>', Updatecurso.as_view()),

    path('deletematricula/<pk>', Deletematricula.as_view()),
    path('deletealumno/<pk>', Deletealumno.as_view()),
    path('deletecurso/<pk>', Deletecurso.as_view())
]

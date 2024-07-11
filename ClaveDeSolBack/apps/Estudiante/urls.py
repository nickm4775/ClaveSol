from django.urls import path
from .views import *

urlpatterns = [
    # Estudiante:
    path('Estudiante', EstudianteListView.as_view()),                      # Listar
    path('Estudiante/<id>', EstudianteView.as_view()),                       # Elemento
    path('EditEstudiante/<id>', EditEstudianteView.as_view()),               # Edit
    path('DeleteEstudiante/<id>', DeleteEstudianteView.as_view()),           # Delete
    path('CreateEstudiante', CreateEstudianteView.as_view()),                # Create
    path('BuscarEstudiante/Search', SearchEstudianteView.as_view()),         # Search
    path('filtrarEstudianteEstudiante/fil', ListNivelView.as_view()),            # Filter
    path('estudiante/<id>/cumple_requisitos_permanecer/', CumpleRequisitosPermanecer.as_view()),  #permanecer
    path('estudiante/<id>/cumple_requisitos_subir/', CumpleRequisitosSubir.as_view()), #subir
    path('estudiantes/', EstudianteDetailView.as_view()),
    path('estudiantesSinNivel/', estudianteSinNivel.as_view()),
]


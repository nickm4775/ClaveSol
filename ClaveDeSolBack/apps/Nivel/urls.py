from django.urls import path
from .views import *

urlpatterns = [
    # Nivel:
    path('Nivel', NivelListView.as_view()),                      # Listar
    path('Nivel/<id>', NivelView.as_view()),                       # Elemento
    path('EditNivel/<id>', EditNivelView.as_view()),               # Edit
    path('DeleteNivel/<id>', DeleteNivelView.as_view()),           # Delete
    path('CreateNivel', CreateNivelView.as_view()),                # Create
    
#     path('BuscarNivel/Search', SearchNivelView.as_view()),         # Search
]


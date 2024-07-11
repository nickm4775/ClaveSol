from django.urls import path
from .views import *

urlpatterns = [
    # Coordinador:
    path('Coordinador', CoordinadorListView.as_view()),                      # Listar
    path('Coordinador/<id>', CoordinadorView.as_view()),                       # Elemento
    path('EditCoordinador/<id>', EditCoordinadorView.as_view()),               # Edit
    path('DeleteCoordinador/<id>', DeleteCoordinadorView.as_view()),           # Delete
    path('CreateCoordinador', CreateCoordinadorView.as_view()),                # Create
    # path('BuscarCoordinador/Search', SearchCoordinadorView.as_view()),         # Search
    # path('filtrarCoordinadorCoordinador/fil', CoordinadorListView.as_view()),            # Filter
    
]


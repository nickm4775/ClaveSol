from django.urls import path
from .views import *

urlpatterns = [
    # Requisito:
    path('Requisito', RequisitoListView.as_view()),                      # Listar
    path('Requisito/<id>', RequisitoView.as_view()),                       # Elemento
    path('EditRequisito/<id>', EditRequisitoView.as_view()),               # Edit
    path('DeleteRequisito/<id>', DeleteRequisitoView.as_view()),           # Delete
    path('CreateRequisito', CreateRequisitoView.as_view()),                # Create
    path('BuscarRequisito/Search', SearchRequisitoView.as_view()),         # Search
    
]


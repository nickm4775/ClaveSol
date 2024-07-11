from django.urls import path
from .views import *

urlpatterns = [
    # User:
    path('User', UserListView.as_view()),                            # Listar
    path('User/<id>', UserView.as_view()),                            # Elemento
    path('UserE/<email>', UserEmail.as_view()),
    path('EditUser/<id>', EditUserView.as_view()),                    # Edit
    # path('EditUserCoor/<id>', EditUserCoordinadorView.as_view()),      # Edit
    # path('EditUserEstudiante/<id>', EditUserEstudianteView.as_view()),       # Edit
    path('DeleteUser/<id>', DeleteUserView.as_view()),                # Delete
    path('BuscarUser/Search', SearchUserView.as_view()),              # Search
    
    # path('filtrarUserCoor/fil', ListCoordinadorView.as_view()),        # Filter
    # path('filtrarUserEstudiante/fil', ListEstudianteView.as_view()),         # Filter
]

from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework import permissions
from .serializers import *
from .models import *
from rest_framework.parsers import MultiPartParser, FormParser
from django.shortcuts import get_object_or_404
from .pagination import SmallSetPagination, MediumSetPagination, LargeSetPagination
from django.db.models import Q
from functools import reduce
from rest_framework import filters


# Create your views here.

# FiltrarNivel
class ListNivelView(APIView):
    permission_classes = (permissions.AllowAny,)
    filter_backends = (filters.SearchFilter, filters.OrderingFilter)
    search_fields = ('nivel',)

    def get(self, request, format=None):
        if Estudiante.objects.all().exists():
            queryset = Estudiante.objects.all()
            nivel_query = request.GET.get('nivel', None)

            if nivel_query:
                queryset = queryset.filter(
                    nivel__nombre__icontains=nivel_query)

            queryset = queryset.order_by('usuario__nombre')
            paginator = SmallSetPagination()
            results = paginator.paginate_queryset(queryset, request)
            serializer = EstudianteListSerializer(results, many=True)

            return paginator.get_paginated_response({'estudianteNivel': serializer.data})
        else:
            return Response({'error': 'ningun estudiante encontrado'}, status=status.HTTP_404_NOT_FOUND)


# Busqueda
class SearchEstudianteView(APIView):
    permission_classes = (permissions.AllowAny,)

    def get(self, request, format=None):
        search_term = request.query_params.get('s')
        matches = Estudiante.objects.filter(
            Q(usuario__nombre__icontains=search_term)
        )
        queryset = matches.order_by('usuario__nombre')
        paginator = SmallSetPagination()
        results = paginator.paginate_queryset(queryset, request)
        serializer = EstudianteListSerializer(results, many=True)

        return paginator.get_paginated_response({'search_estudiante': serializer.data})


# Listar
class EstudianteListView(APIView):
    permission_classes = (permissions.AllowAny,)

    def get(self, request, format=None):
        if Estudiante.objects.all().exists():
            estudiante = Estudiante.objects.all()

            queryset = estudiante.order_by('nombre')
            paginator = SmallSetPagination()
            results = paginator.paginate_queryset(queryset, request)
            serializer = EstudianteListSerializer(results, many=True)

            return paginator.get_paginated_response({'Estudiante': serializer.data})
        else:
            return Response({'error': 'ningun estudiante encontrado'}, status=status.HTTP_404_NOT_FOUND)


# Obtener
class EstudianteView(APIView):
    permission_classes = (permissions.AllowAny,)

    def get(self, request, id, format=None):
        if Estudiante.objects.filter(id=id).exists():
            estudiante = Estudiante.objects.get(id=id)
            serializer = EstudianteSerializer(estudiante)

            return Response({'Estudiante': serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'ningun estudiante encontrado'}, status=status.HTTP_404_NOT_FOUND)


# Editar
class EditEstudianteView(APIView):
    permission_classes = (permissions.AllowAny,)
    parser_classes = [MultiPartParser, FormParser]

    def put(self, request, id, format=None):
        data = self.request.data
        estudiante = get_object_or_404(Estudiante, id=id)

        nombre = data.get('nombre', None)
        if nombre is not None:
            estudiante.nombre = nombre

        nivel = data.get('nivel', None)
        if nivel is not None:
            estudiante.nivel = nivel

        # Actualizar requisitos cumplidos (esto es solo un ejemplo, ajusta según sea necesario)
        requisitos_cumplidos = data.get('requisitos_cumplidos', None)
        if requisitos_cumplidos is not None:
            estudiante.requisitos_cumplidos.set(requisitos_cumplidos)

        estudiante.save()

        updated_fields = [key for key in data.keys() if key in [
            'nivel', 'requisitos_cumplidos']]
        return Response({'success': 'Estudiante editado', 'estudiante_id': estudiante.id, 'updated_fields': updated_fields})


# Borrar
class DeleteEstudianteView(APIView):
    permission_classes = (permissions.AllowAny,)

    def delete(self, request, id, format=None):
        estudiante = Estudiante.objects.get(id=id)
        estudiante.delete()
        return Response({'success': 'Estudiante eliminado'})


# Crear
class CreateEstudianteView(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        # Obtén los datos de la solicitud
        data = request.data

        # Crea una instancia del serializer con los datos
        serializer = EstudianteSerializer(data=data)

        # Valida los datos
        if serializer.is_valid():
            # Guarda el nuevo estudiante en la base de datos
            serializer.save()

            # Devuelve una respuesta exitosa
            return Response({'success': 'Estudiante creado'}, status=status.HTTP_201_CREATED)
        else:
            # Prepara un mensaje de error más detallado
            error_messages = {}
            for field, errors in serializer.errors.items():
                if isinstance(errors, list):  # Si hay múltiples errores para un campo
                    error_messages[field] = ', '.join(errors)
                else:
                    error_messages[field] = errors

            # Devuelve una respuesta con errores de validación si los datos no son válidos
            return Response(error_messages, status=status.HTTP_400_BAD_REQUEST)

#Para saber si cumple los requisitos
#@api_view(['GET'])
class CumpleRequisitosPermanecer(APIView):
    def get(request, estudiante_id):
        estudiante = Estudiante.objects.get(pk=estudiante_id)
        cumple = estudiante.cumple_requisitos_permanecer()
        return Response({'cumple_requisitos_permanecer': cumple})

#@api_view(['GET'])
class CumpleRequisitosSubir(APIView):
    def get(request, estudiante_id):
        estudiante = Estudiante.objects.get(pk=estudiante_id)
        cumple = estudiante.cumple_requisitos_subir()
        return Response({'cumple_requisitos_subir': cumple})
       
       
class EstudianteDetailView(APIView):
    permission_classes = (permissions.AllowAny,)

    def get(self, request, *args, **kwargs):
        estudiantes = Estudiante.objects.select_related('nombre').all()
        
        
        estudiantes_data = []
        for estudiante in estudiantes:
 
            requisitos_permanecer = Requisito.objects.filter(requisitos_nivel=estudiante.nivel_id, permanecer=True).values_list('nombre', flat=True),
            requisitos_subir = Requisito.objects.filter(requisitos_nivel=estudiante.nivel_id, subir=True).values_list('nombre', flat=True),

            estudiante_data = {
                'id': estudiante.id,
                'nivel_id': estudiante.nivel_id,
                'nivel_nombre':estudiante.nivel.nombre,
                'requisitos_cumplidos_permanecer':  requisitos_permanecer,             #list(estudiante.requisitos_cumplidos_permanecer.values_list('nombre', flat=True)),
                'requisitos_cumplidos_subir':   requisitos_subir   ,              #list(estudiante.requisitos_cumplidos_subir.values_list('nombre', flat=True)),
                'requisitos_cumplidos': list(estudiante.requisitos_cumplidos.values_list('nombre', flat=True)),
                'nombre': estudiante.nombre.id,  # Asumiendo que 'nombre' es la relación con UserAccount
                'email':estudiante.nombre.email,
                'first_name': estudiante.nombre.first_name,
                'last_name': estudiante.nombre.last_name,
                'is_active': estudiante.nombre.is_active,
                'is_staff': estudiante.nombre.is_staff,
                'is_coordinador': estudiante.nombre.is_coordinador,
                'is_admin': estudiante.nombre.is_admin,
                'is_estudiante': estudiante.nombre.is_estudiante,
                'last_login': estudiante.nombre.last_login,
            }
            estudiantes_data.append(estudiante_data)
        return Response({'estudiantes': estudiantes_data})

class estudianteSinNivel(APIView):
    permission_classes = (permissions.AllowAny,)

    def get(self, request):
        # Filtra estudiantes que tienen is_estudiante=True en UserAccount y nivel=NULL en Estudiante
        estudiantes_sin_nivel = Estudiante.objects.filter(nombre__is_estudiante=True, nivel__isnull=True)
        students_data = [{"id": estudiante.id, "email": estudiante.nombre.email, "name": f"{estudiante.nombre.first_name} {estudiante.nombre.last_name}"} for estudiante in estudiantes_sin_nivel]
        return Response({"students": students_data})

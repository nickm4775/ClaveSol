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

# # FiltrarNivel
# class ListNivelView(APIView):
#     permission_classes = (permissions.AllowAny,)
#     filter_backends = (filters.SearchFilter, filters.OrderingFilter)
#     search_fields = ('nivel',)

#     def get(self, request, format=None):
#         if Coordinador.objects.all().exists():
#             queryset = Coordinador.objects.all()
#             nivel_query = request.GET.get('nivel', None)

#             if nivel_query:
#                 queryset = queryset.filter(
#                     nivel__nombre__icontains=nivel_query)

#             queryset = queryset.order_by('usuario__nombre')
#             paginator = SmallSetPagination()
#             results = paginator.paginate_queryset(queryset, request)
#             serializer = CoordinadorListSerializer(results, many=True)

#             return paginator.get_paginated_response({'CoordinadorNivel': serializer.data})
#         else:
#             return Response({'error': 'ningun coordinador encontrado'}, status=status.HTTP_404_NOT_FOUND)


# Busqueda
# class SearchCoordinadorView(APIView):
#     permission_classes = (permissions.AllowAny,)

#     def get(self, request, format=None):
#         search_term = request.query_params.get('s')
#         matches = Coordinador.objects.filter(
#             Q(usuario__nombre__icontains=search_term)
#         )
#         queryset = matches.order_by('usuario__nombre')
#         paginator = SmallSetPagination()
#         results = paginator.paginate_queryset(queryset, request)
#         serializer = CoordinadorListSerializer(results, many=True)

#         return paginator.get_paginated_response({'search_Coordinador': serializer.data})


# Listar
class CoordinadorListView(APIView):
    permission_classes = (permissions.AllowAny,)

    def get(self, request, format=None):
        if Coordinador.objects.all().exists():
            coordinador = Coordinador.objects.all()

            queryset = coordinador.order_by('nombre')
            paginator = SmallSetPagination()
            results = paginator.paginate_queryset(queryset, request)
            serializer = CoordinadorListSerializer(results, many=True)

            return paginator.get_paginated_response({'Coordinador': serializer.data})
        else:
            return Response({'error': 'ningun coordinador encontrado'}, status=status.HTTP_404_NOT_FOUND)


# Obtener
class CoordinadorView(APIView):
    permission_classes = (permissions.AllowAny,)

    def get(self, request, id, format=None):
        if Coordinador.objects.filter(id=id).exists():
            coordinador = Coordinador.objects.get(id=id)
            serializer = CoordinadorSerializer(coordinador)

            return Response({'Coordinador': serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'ningun coordinador encontrado'}, status=status.HTTP_404_NOT_FOUND)


# Editar
class EditCoordinadorView(APIView):
    permission_classes = (permissions.AllowAny,)
    parser_classes = [MultiPartParser, FormParser]

    def put(self, request, id, format=None):
        data = self.request.data
        coordinador = get_object_or_404(Coordinador, id=id)

        nombre = data.get('nombre', None)
        if nombre is not None:
            coordinador.nombre = nombre

        nivel = data.get('nivel', None)
        if nivel is not None:
            coordinador.nivel = nivel

       

        coordinador.save()

        updated_fields = [key for key in data.keys() if key in [
            'nivel', 'nombre']]
        return Response({'success': 'Coordinador editado', 'Coordinador_id': coordinador.id, 'updated_fields': updated_fields})


# Borrar
class DeleteCoordinadorView(APIView):
    permission_classes = (permissions.AllowAny,)

    def delete(self, request, id, format=None):
        coordinador = Coordinador.objects.get(id=id)
        coordinador.delete()
        return Response({'success': 'Coordinador eliminado'})


# Crear
class CreateCoordinadorView(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        # Obtén los datos de la solicitud
        data = request.data

        # Crea una instancia del serializer con los datos
        serializer = CoordinadorSerializer(data=data)

        # Valida los datos
        if serializer.is_valid():
            # Guarda el nuevo Coordinador en la base de datos
            serializer.save()

            # Devuelve una respuesta exitosa
            return Response({'success': 'Coordinador creado'}, status=200)

        # Devuelve una respuesta con errores de validación si los datos no son válidos
        return Response(serializer.errors, status=404)

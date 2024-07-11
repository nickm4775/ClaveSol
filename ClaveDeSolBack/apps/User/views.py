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


# FiltrarCoordinador
# class ListCoordinadorView(APIView):
#     permission_classes = (permissions.AllowAny,)
#     filter_backends = (filters.SearchFilter, filters.OrderingFilter)
#     search_fields = ('is_coordinador',)

#     def get(self, request, format=None):
#         if User.objects.all().exists():
#             queryset = User.objects.all()
#             is_coordinador_query = request.GET.get('coor', None)

#             if is_coordinador_query is not None:
#                 is_coordinador_query = is_coordinador_query.lower() == 'true'
#                 queryset = queryset.filter(is_coordinador=is_coordinador_query)

#             queryset = queryset.order_by('first_name')
#             paginator = SmallSetPagination()
#             results = paginator.paginate_queryset(queryset, request)
#             serializer = UserSerializer(results, many=True)

#             return paginator.get_paginated_response({'Coordinador(es)': serializer.data})
#         else:
#             return Response({'error': 'ningun user encontrado'}, status=status.HTTP_404_NOT_FOUND)


# Filtrarestudiante
# class ListEstudianteView(APIView):
#     permission_classes = (permissions.AllowAny,)
#     filter_backends = (filters.SearchFilter, filters.OrderingFilter)
#     search_fields = ('is_estudiante',)

#     def get(self, request, format=None):
#         if User.objects.all().exists():
#             queryset = User.objects.all()
#             is_estudiante_query = request.GET.get('mem', None)

#             if is_estudiante_query is not None:
#                 is_estudiante_query = is_estudiante_query.lower() == 'true'
#                 queryset = queryset.filter(is_estudiante=is_estudiante_query)

#             queryset = queryset.order_by('first_name')
#             paginator = SmallSetPagination()
#             results = paginator.paginate_queryset(queryset, request)
#             serializer = UserSerializer(results, many=True)

#             return paginator.get_paginated_response({'estudiante(s)': serializer.data})
#         else:
#             return Response({'error': 'ningun user encontrado'}, status=status.HTTP_404_NOT_FOUND)


# Busqueda
class SearchUserView(APIView):
    permission_classes = (permissions.AllowAny,)

    def get(self, request, format=None):
        serch_term = request.query_params.get('s')
        matches = User.objects.filter(
            Q(email__icontains=serch_term) |
            Q(first_name__icontains=serch_term) |
            Q(last_name__icontains=serch_term)
        )
        queryset = matches.order_by('first_name')
        paginator = SmallSetPagination()
        results = paginator.paginate_queryset(queryset, request)
        serializer = UserSerializer(results, many=True)

        return paginator.get_paginated_response({'search_user': serializer.data})


# Listar
class UserListView(APIView):
    permission_classes = (permissions.AllowAny,)

    def get(self, request, format=None):
        if User.objects.all().exists():
            user = User.objects.all()

            queryset = user.order_by('first_name')
            paginator = SmallSetPagination()
            results = paginator.paginate_queryset(queryset, request)
            serializer = UserSerializer(results, many=True)

            return paginator.get_paginated_response({'User': serializer.data})
        else:
            return Response({'error': 'ningun user encontrado'}, status=status.HTTP_404_NOT_FOUND)


# Obtener
class UserView(APIView):
    permission_classes = (permissions.AllowAny,)

    def get(self, request, id, format=None):
        if User.objects.filter(id=id).exists():
            user = User.objects.get(id=id)
            serializer = UserSerializer(user)

            return Response({'User': serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'ningun user encontrado'}, status=status.HTTP_404_NOT_FOUND)

class UserEmail(APIView):
    permission_classes = (permissions.AllowAny,)

    def get(self, request, email, format=None):
        if User.objects.filter(email=email).exists():
            user = User.objects.get(email=email)
            serializer = UserSerializer(user)

            return Response({'User': serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'ningun user encontrado'}, status=status.HTTP_404_NOT_FOUND)

            


# Borrar
class DeleteUserView(APIView):
    permission_classes = (permissions.AllowAny,)

    def delete(self, request, id, format=None):
        user = User.objects.get(id=id)
        user.delete()
        return Response({'success': 'User eliminado'})


# Editar
class EditUserView(APIView):
    permission_classes = (permissions.AllowAny,)
    parser_classes = [MultiPartParser, FormParser]

    def put(self, request, id, format=None):
        data = self.request.data
        user = get_object_or_404(User, id=id)

        email = data.get('email', None)
        if email is not None:
            user.email = email

        first_name = data.get('first_name', None)
        if first_name is not None:
            user.first_name = first_name

        last_name = data.get('last_name', None)
        if last_name is not None:
            user.last_name = last_name



        user.save()

        updated_fields = [key for key in data.keys() if key in [
            'email', 'first_name', 'last_name', 'birthday']]
        return Response({'success': 'User editado', 'user_id': user.id, 'updated_fields': updated_fields})



# estudiante
# class EditUserEstudianteView(APIView):
#     permission_classes = (permissions.AllowAny,)
#     parser_classes = [MultiPartParser, FormParser]

#     def put(self, request, id, format=None):
#         data = self.request.data
#         user = get_object_or_404(User, id=id)

#         is_estudiante = data.get('is_estudiante', None)
#         if is_estudiante is not None:
#             user.is_estudiante = is_estudiante

#         user.save()

#         updated_fields = [key for key in data.keys() if key in [
#             'is_estudiante']]
#         return Response({'success': 'User editado', 'user_id': user.id, 'updated_fields': updated_fields})


# # Coodinador
# class EditUserCoordinadorView(APIView):
#     permission_classes = (permissions.AllowAny,)
#     parser_classes = [MultiPartParser, FormParser]

#     def put(self, request, id, format=None):
#         data = self.request.data
#         user = get_object_or_404(User, id=id)

#         is_coordinador = data.get('is_coordinador', None)
#         if is_coordinador is not None:
#             user.is_coordinador = is_coordinador

#         user.save()

#         updated_fields = [key for key in data.keys() if key in [
#             'is_coordinador']]
#         return Response({'success': 'User editado', 'user_id': user.id, 'updated_fields': updated_fields})

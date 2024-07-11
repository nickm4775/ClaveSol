from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status, permissions, filters
from .serializers import *
from .models import Nivel
from .pagination import SmallSetPagination
from django.db.models import Q
from rest_framework.parsers import MultiPartParser, FormParser

class SearchNivelView(APIView):
    permission_classes = (permissions.AllowAny,)

    def get(self, request, format=None):
        search_term = request.query_params.get('s')
        matches = Nivel.objects.filter(Q(nombre__icontains=search_term))
        paginator = SmallSetPagination()
        results = paginator.paginate_queryset(matches, request)
        serializer = NivelSerializer(results, many=True)
        return paginator.get_paginated_response({'search_nivel': serializer.data})

class NivelListView(APIView):
    permission_classes = (permissions.AllowAny,)

    def get(self, request, format=None):
        queryset = Nivel.objects.all()
        paginator = SmallSetPagination()
        results = paginator.paginate_queryset(queryset, request)
        serializer = NivelSerializer(results, many=True)
        return paginator.get_paginated_response({'Nivel': serializer.data})

class NivelView(APIView):
    permission_classes = (permissions.AllowAny,)

    def get(self, request, id, format=None):
        nivel = get_object_or_404(Nivel, id=id)
        serializer = NivelSerializer(nivel)
        return Response({'Nivel': serializer.data})

class EditNivelView(APIView):
    permission_classes = (permissions.AllowAny,)
    parser_classes = [MultiPartParser, FormParser]

    def put(self, request, id, format=None):
        nivel = get_object_or_404(Nivel, id=id)
        serializer = NivelSerializer(nivel, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'success': 'Nivel editado'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DeleteNivelView(APIView):
    permission_classes = (permissions.AllowAny,)

    def delete(self, request, id, format=None):
        nivel = get_object_or_404(Nivel, id=id)
        nivel.delete()
        return Response({'success': 'Nivel eliminado'}, status=status.HTTP_200_OK)

class CreateNivelView(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, *args, **kwargs):
        serializer = NivelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'success': 'Nivel creado'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


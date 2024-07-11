from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status, permissions, filters
from .serializers import *
from .models import Requisito
from .pagination import SmallSetPagination
from django.db.models import Q
from rest_framework.parsers import MultiPartParser, FormParser

class SearchRequisitoView(APIView):
    permission_classes = (permissions.AllowAny,)

    def get(self, request, format=None):
        search_term = request.query_params.get('s')
        matches = Requisito.objects.filter(Q(nombre__icontains=search_term))
        paginator = SmallSetPagination()
        results = paginator.paginate_queryset(matches, request)
        serializer = RequisitoSerializer(results, many=True)
        return paginator.get_paginated_response({'search_requisito': serializer.data})

class RequisitoListView(APIView):
    permission_classes = (permissions.AllowAny,)

    def get(self, request, format=None):
        queryset = Requisito.objects.all()
        paginator = SmallSetPagination()
        results = paginator.paginate_queryset(queryset, request)
        serializer = RequisitoSerializer(results, many=True)
        return paginator.get_paginated_response({'Requisito': serializer.data})

class RequisitoView(APIView):
    permission_classes = (permissions.AllowAny,)

    def get(self, request, id, format=None):
        requisito = get_object_or_404(Requisito, id=id)
        serializer = RequisitoSerializer(requisito)
        return Response({'Requisito': serializer.data})

class EditRequisitoView(APIView):
    permission_classes = (permissions.AllowAny,)
    parser_classes = [MultiPartParser, FormParser]

    def put(self, request, id, format=None):
        requisito = get_object_or_404(Requisito, id=id)
        serializer = RequisitoSerializer(requisito, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'success': 'Requisito editado'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DeleteRequisitoView(APIView):
    permission_classes = (permissions.AllowAny,)

    def delete(self, request, id, format=None):
        requisito = get_object_or_404(Requisito, id=id)
        requisito.delete()
        return Response({'success': 'Requisito eliminado'}, status=status.HTTP_200_OK)

class CreateRequisitoView(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = RequisitoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'success': 'Requisito creado'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

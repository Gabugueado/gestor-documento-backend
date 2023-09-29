from django.shortcuts import redirect, render
from rest_framework import generics
from .models import Document
from .serializers import DocumentSerializer
from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from .models import Document
from .serializers import DocumentSerializer
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.middleware.csrf import get_token
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.http import FileResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import base64
from .models import Document  # Asegúrate de importar tu modelo Document

# Create your views here.

class DocumentCreateView(generics.CreateAPIView):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer

class DocumentListView(generics.ListAPIView):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer
    
    def list(self, request, *args, **kwargs):
        documents = self.get_queryset()
        if not request.user.is_authenticated:
            return Response({"detail": "Debes iniciar sesión para listar los documentos."}, status=status.HTTP_403_FORBIDDEN)
        if not documents.exists():
            return Response({"detail": "No se encontraron documentos."}, status=status.HTTP_404_NOT_FOUND)
        serializer = self.get_serializer(documents, many=True)
        return Response(serializer.data)



class DocumentBase64View(APIView):
    def get(self, request, document_id):
        try:
            document = Document.objects.get(id=document_id)
            # Obtener el contenido del archivo en base64
            with open(document.file.path, 'rb') as file:
                base64_content = base64.b64encode(file.read()).decode('utf-8')

            # Crear una respuesta JSON con el contenido en base64
            response_data = {
                'id': document.id,
                'title': document.title,
                'content': document.content,
                'base64_content': base64_content,
            }

            return Response(response_data)
        except Document.DoesNotExist:
            return Response({"detail": "Documento no encontrado."}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            print(e)
            return Response({"detail": "Error al obtener el contenido en base64."}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class DocumentUpdateView(generics.UpdateAPIView):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer


    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        print(self)
        if instance is None:
            return Response({"detail": "El documento no se encontró."}, status=status.HTTP_404_NOT_FOUND)
        
        # Actualizar el objeto 'Document' con los datos del cuerpo de la solicitud
        serializer = self.get_serializer(instance, data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DocumentDeleteView(generics.DestroyAPIView):
    queryset = Document.objects.all()


    def perform_destroy(self, instance):
        # Eliminar el archivo asociado al documento
        instance.file.delete()
        # Eliminar el registro del documento
        instance.delete()

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance is None:
            return Response({"detail": "El documento no se encontró."}, status=status.HTTP_404_NOT_FOUND)
        
        # Verifica si el usuario está autenticado (esto es solo un ejemplo)
        if not request.user.is_authenticated:
            return Response({"detail": "Debes iniciar sesión para eliminar documentos."}, status=status.HTTP_403_FORBIDDEN)

        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)


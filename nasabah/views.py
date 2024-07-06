from rest_framework import status, permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from django.http import Http404
from rest_framework.views import APIView
from .models import Nasabah, Jaminan, BarangGadai, Peminjaman
from .serializers import NasabahSerializer, JaminanSerializer, BarangGadaiSerializer, PeminjamanSerializer

# Create your views here.
@api_view(['GET', 'POST']) # decorator
@permission_classes([permissions.AllowAny])
def nasabah_list(request, format=None):

    if request.method == 'GET':
        nasabah = Nasabah.objects.all()
        serializer = NasabahSerializer(nasabah, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = NasabahSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def nasabah_detail(request, pk, format=None):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        nasabah = Nasabah.objects.get(pk=pk)
    except Nasabah.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = NasabahSerializer(nasabah)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = NasabahSerializer(nasabah, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        nasabah.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# view untuk produk dengan class base view
class JaminanList(APIView):

    permission_classes = [permissions.AllowAny]
    def get(self, request, format=None):
        jaminan = Jaminan.objects.all()
        serializer = JaminanSerializer(jaminan, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = JaminanSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class JaminanDetail(APIView):
    """
    ambil data, edit atau hapus data
    """
    parser_classes = [permissions.AllowAny]
    def get_object(self, pk):
        try:
            return Jaminan.objects.get(pk=pk)
        except Jaminan.DoesNotExist:
            raise Http404
        
    def get(self, request, pk, format=None):
        jaminan = self.get_object(pk)
        serializer = JaminanSerializer(jaminan)
        return Response(serializer.data)
    
    def put(self, request, pk, format=None):
        jaminan = self.get_object(pk)
        serializer = JaminanSerializer(jaminan, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None):
        jaminan = self.get_object(pk=pk)
        jaminan.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
@api_view(['GET', 'POST']) # decorator
@permission_classes([permissions.AllowAny])
def baranggadai_list(request, format=None):

    if request.method == 'GET':
        baranggadai = BarangGadai.objects.all()
        serializer = BarangGadaiSerializer(baranggadai, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = BarangGadaiSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET', 'POST']) # decorator
@permission_classes([permissions.AllowAny])
def peminjaman_list(request, format=None):

    if request.method == 'GET':
        peminjaman = Peminjaman.objects.all()
        serializer = PeminjamanSerializer(peminjaman, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = PeminjamanSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

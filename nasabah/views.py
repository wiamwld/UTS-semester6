from rest_framework import viewsets
from .models import Nasabah
from .serializers import NasabahSerializer

class NasabahViewSet(viewsets.ModelViewSet):
    queryset = Nasabah.objects.all()
    serializer_class = NasabahSerializer

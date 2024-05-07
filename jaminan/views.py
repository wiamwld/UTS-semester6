from rest_framework import viewsets
from .models import Jaminan
from .serializers import JaminanSerializer

class JaminanViewSet(viewsets.ModelViewSet):
    queryset = Jaminan.objects.all()
    serializer_class = JaminanSerializer

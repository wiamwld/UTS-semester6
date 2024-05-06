from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import NasabahViewSet


router = DefaultRouter()
router.register(r'nasabah', NasabahViewSet) 


urlpatterns = [
    path('nasabah/', include(router.urls)),
    
]
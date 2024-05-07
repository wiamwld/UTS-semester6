from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import JaminanViewSet

router = DefaultRouter()
router.register(r'jaminan', JaminanViewSet)


urlpatterns = [
    path('jaminan/', include(router.urls)),
]

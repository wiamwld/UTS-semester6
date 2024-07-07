##from django.urls import path, include
##from rest_framework.routers import DefaultRouter
##from .views import NasabahViewSet


##router = DefaultRouter()
##router.register(r'nasabah', NasabahViewSet) 


##urlpatterns = [
  ##  path('nasabah/', include(router.urls)),
    
##]

from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('nasabah/', views.nasabah_list),
    path('nasabah/<int:pk>/', views.nasabah_detail),
    path('jaminan/', views.JaminanList.as_view()),
    path('jaminan/<int:pk>/', views.JaminanDetail.as_view()),
    path('baranggadai/', views.baranggadai_list),
    path('pinjaman/', views.pinjaman_list),

]

urlpatterns = format_suffix_patterns(urlpatterns)
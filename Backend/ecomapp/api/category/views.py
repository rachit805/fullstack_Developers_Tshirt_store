from rest_framework import viewsets

from .serializers import CategorySerializer
from .models import Category

class CategoryViewSets(viewsets.ModelViewSet):
    queryset = Category.objects.all().order_by('name')
    serilaizer_class = CategorySerializer
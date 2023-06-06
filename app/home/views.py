from rest_framework import viewsets, status
from .serializers import DisciplinaSerializer
from .models import Disciplina
from rest_framework.decorators import action
from rest_framework.response import Response

class DisciplinaViewSet(viewsets.ModelViewSet):
  queryset = Disciplina.objects.all()
  serializer_class = DisciplinaSerializer
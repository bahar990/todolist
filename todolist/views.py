from django.shortcuts import render

# Create your views here.
from .models import Todolist
from rest_framework import viewsets
from .serilaizers import Todolistserializer



class Todolistview(viewsets.ModelViewSet):
    queryset=Todolist.objects.all()
    serializer_class=Todolistserializer
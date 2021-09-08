from django.shortcuts import render

# Create your views here.
from .models import Events
from .serializers import LeadSerializer
from rest_framework import generics

class LeadListCreate(generics.ListCreateAPIView):
    queryset = Events.objects.all()
    serializer_class = LeadSerializer
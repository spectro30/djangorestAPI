from django.shortcuts import render

from rest_framework import generics
from .serializers import InfoSerializer
from .models import Info


class CreateView(generics.ListCreateAPIView):
    queryset = Info.objects.all()
    serializer_class = InfoSerializer

    def perform_create(self, serializer):
        serializer.save()


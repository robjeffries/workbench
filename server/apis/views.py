from django.shortcuts import render, get_object_or_404
from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions
from .models import Log
from .serializers import LogSerializer

class LogViewSet(ModelViewSet):
    serializer_class = LogSerializer

    def get_object(self):
        return get_object_or_404(Log, id=self.request.query_params.get("id"))

    def get_queryset(self):
        #return Log.objects.filter({})
        return Log.objects.all()
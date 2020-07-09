from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from .serializers import postSerializer,commentSerializer
from .models import post,comment


class postViewSet(viewsets.ModelViewSet):
    queryset = post.objects.all()
    serializer_class = postSerializer
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class commentViewSet(viewsets.ModelViewSet):
    queryset = comment.objects.all()
    serializer_class = commentSerializer
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
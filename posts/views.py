from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from .serializers import postSerializer
from .models import post


class postViewSet(viewsets.ModelViewSet):
    queryset = post.objects.all()
    serializer_class = postSerializer
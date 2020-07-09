from rest_framework import serializers

from .models import post,comment
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','username')

class postSerializer(serializers.HyperlinkedModelSerializer):
    user=UserSerializer(read_only=True)
    class Meta:
        model = post
        fields = ('user','desc')
    

class commentSerializer(serializers.HyperlinkedModelSerializer):
    # user=UserSerializer(read_only=True)
    class Meta:
        model = comment
        fields = ('post','comment')
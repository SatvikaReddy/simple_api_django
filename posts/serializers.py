from rest_framework import serializers

from .models import post

class postSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = post
        fields = ('userid','user','desc')
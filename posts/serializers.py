from rest_framework import serializers

from .models import post,comment

class postSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = post
        fields = ('userid','user','desc')

class commentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = comment
        fields = ('user','comment')
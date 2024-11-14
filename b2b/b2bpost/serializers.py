# serializers.py
from rest_framework import serializers
from .models import B2BPost

class B2BPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = B2BPost
        fields = ['content','created_at','facts','nah_bro']



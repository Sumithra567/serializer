from rest_framework import serializers
from .models import USERS

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=USERS
        fields=["id","name","mob"]

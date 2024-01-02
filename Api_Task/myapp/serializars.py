from .models import *
from rest_framework import serializers
from django.contrib.auth.models import User


class UserSerializar(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password' ]
        
    def create(self, validated_data):
        user = User.objects.create(username=validated_data['username'])
        user.set_password(validated_data['password'])
        user.save()
        return user



# --------------------------------------------------------

class PersonSerializar(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = "__all__"
        
class  ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = "__all__"
        
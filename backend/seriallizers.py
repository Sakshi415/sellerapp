from rest_framework import serializers
from . import models
import datetime


class CreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Create
        fields = '__all__'

    def create(self, validated_data):
        return models.Create.objects.create(**validated_data) 
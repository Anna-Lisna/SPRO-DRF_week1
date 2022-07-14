from django.core.validators import MaxValueValidator, MinValueValidator
from rest_framework import serializers

from tutorial.models import Store


class StoreSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    description = serializers.CharField(max_length=800)
    rating = serializers.IntegerField(validators=[MaxValueValidator(100), MinValueValidator(1)])

    def create(self, validated_data):
        store = Store.objects.create(**validated_data)
        return store

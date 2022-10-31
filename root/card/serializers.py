from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from .models import Card
from rest_framework.validators import UniqueTogetherValidator


class PersonalCardSerializer(ModelSerializer):
    class Meta:
        model = Card
        fields = ('id', 'name', 'middle_name', 'last_name',
                  'age', 'gender', 'vaccinated')
        read_only = ('age', 'vaccinated', 'gender')

    def create(self, validated_data):
        try:
            return Card.objects.get(**validated_data)

        except Card.DoesNotExist:
            return Card.objects.create(**validated_data)

    @staticmethod
    def validate_age(value: int):
        """
        Check that age is meaningful for a living person
        """
        if 12 <= value <= 90:
            return value
        raise serializers.ValidationError("Age must be in the following range (12, 90)")
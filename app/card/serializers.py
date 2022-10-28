from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from .models import Card
from rest_framework.validators import UniqueTogetherValidator


class PersonalCardSerializer(ModelSerializer):
    class Meta:
        model = Card
        fields = ('id', 'name', 'middle_name', 'last_name',
                  'age', 'gender', 'vaccinated')

    def create(self, validated_data):
        try:
            value = Card.objects.get(name=validated_data['name'], middle_name=validated_data['middle_name'],
                                     last_name=validated_data['last_name'])
        except Card.DoesNotExist:
            return Card.objects.create(**validated_data)
        else:
            return value

    @staticmethod
    def validate_age(value: int):
        """
        Check that age is meaningful for a living person
        """
        if 12 <= value <= 90:
            return value
        raise serializers.ValidationError("Age must be in the following range (12, 90)")

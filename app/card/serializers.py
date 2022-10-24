from rest_framework.serializers import ModelSerializer
from .models import Card
from rest_framework.validators import UniqueTogetherValidator


class PersonalCardSerializer(ModelSerializer):
    class Meta:
        model = Card
        fields = ('id', 'name', 'middle_name', 'last_name',
                  'age', 'gender', 'vaccinated')

    def create(self, validated_data):
        instance, _ = Card.objects.get_or_create(**validated_data)
        return instance

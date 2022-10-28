from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import PersonalCardSerializer
from .models import Card


class PersonalCardAPIView(APIView):
    serializer_class = PersonalCardSerializer

    def get(self, request):
        personal_cards = Card.objects.all()
        serializer = self.serializer_class(personal_cards, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = PersonalCardSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

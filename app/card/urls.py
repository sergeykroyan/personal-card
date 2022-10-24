from django.urls import path
from .views import PersonalCardAPIView

urlpatterns = [
    path('api/personal_cards/', PersonalCardAPIView.as_view()),
]


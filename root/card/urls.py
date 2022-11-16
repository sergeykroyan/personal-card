from django.urls import path
from .views import PersonalCardAPIView

app_name = 'card'

urlpatterns = [
    path('personal_cards/', PersonalCardAPIView.as_view(), name='personal_cards'),
]


from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Card


class PersonalCardTests(APITestCase):
    url = reverse('personal_cards')
    data = {'name': 'Vanya',
            'middle_name': 'Petrosi',
            'last_name': 'Petrosyan',
            'age': 61,
            'gender': 'M',
            'vaccinated': 'Y'}

    def test_get_personal_cards(self):
        """
        Make sure we can get personal cards.
        """
        url = reverse('personal_cards')
        response = self.client.get(url, fomrat='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post_personal_card(self):
        """
        Make sure if the data exists it will be returned otherwise new one will be created.
        """
        response = self.client.post(self.url, self.data, fomrat='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        response = self.client.post(self.url, self.data, fomrat='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.data['age'] = 19
        response = self.client.post(self.url, self.data, fomrat='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['age'], 61)

    def test_wrong_data_post(self):
        """
        Make sure that will return an error if the data is incorrect.
        """
        self.data['age'] = -20
        response = self.client.post(self.url, self.data, fomrat='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient

account_data = {
    "accountNumber": 0,
    "accountType": "D",
    "balance": 100.0
}

new_account_data = {
    "balance": 200.0
}

card_data = {
    "accountID": 1,
    "cardNumber": 587401239854,
    "holder": "CARLOS ARNULFO GONZALEZ RODRIGUEZ"
}

new_card_data = {
    "holder": "CHARLY ARNULFO GONZALEZ RODRIGUEZ"
}
class AccountTest(TestCase):
    def test_create_account(self):
        client = APIClient()
        response = client.post('/api/account/', account_data, format='json')
        self.assertEqual(status.HTTP_201_CREATED, response.status_code)

    def test_get_account(self):
        client = APIClient()
        client.post('/api/account/', account_data, format='json')
        response = client.get('/api/account/')
        self.assertEqual(status.HTTP_200_OK, response.status_code)

    def test_delete_account(self):
        client = APIClient()
        client.post('/api/account/', account_data, format='json')
        response = client.delete('/api/account/1/')
        self.assertEqual(status.HTTP_204_NO_CONTENT, response.status_code)
    
    def test_update_account(self):
        client = APIClient()
        client.post('/api/account/', account_data, format='json')
        response = client.put('/api/account/1/', new_account_data, format='json')
        self.assertEqual(status.HTTP_200_OK, response.status_code)


class CardTest(TestCase):
    def test_create_card(self):
        client = APIClient()
        response = client.post('/api/account/', card_data, format='json')
        self.assertEqual(status.HTTP_201_CREATED, response.status_code)

    def test_get_card(self):
        client = APIClient()
        client.post('/api/account/', card_data, format='json')
        response = client.get('/api/account/')
        self.assertEqual(status.HTTP_200_OK, response.status_code)

    def test_delete_card(self):
        client = APIClient()
        client.post('/api/account/', card_data, format='json')
        response = client.delete('/api/account/1/')
        self.assertEqual(status.HTTP_204_NO_CONTENT, response.status_code)
    
    def test_update_card(self):
        client = APIClient()
        client.post('/api/account/', card_data, format='json')
        response = client.put('/api/account/1/', new_card_data, format='json')
        self.assertEqual(status.HTTP_200_OK, response.status_code)
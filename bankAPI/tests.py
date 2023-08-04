from django.test import TestCase
from rest_framework import status
from django.test import TestCase
from rest_framework.test import APIClient


newUser = {
    "id": 1,
    "name": "CARLOS ARNULFO",
    "lastName": "GONALEZ RODRIGUEZ",
    "address": "Carretera al Castillo 2200 El Quince, 45680 El Salto, Jal.",
    "phoneNumber": 3331234567890,
    "email": "carlos.arnulfo@ibm.com",
    "genre": "M",
}

updateUser = {"phoneNumber": 3331134568891}

getUser = {
    "id": 1,
    "name": "CARLOS ARNULFO",
    "lastName": "GONALEZ RODRIGUEZ",
    "address": "Carretera al Castillo 2200 El Quince, 45680 El Salto, Jal.",
    "phoneNumber": 3331134568891,
    "email": "carlos.arnulfo@ibm.com",
    "genre": "M",
}

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


class UserTest(TestCase):
    def testShouldAddUser(self):
        client = APIClient()
        response = client.post("/api/user/", newUser, format="json")
        self.assertEqual(status.HTTP_201_CREATED, response.status_code)

    def testShouldUpdateUser(self):
        client = APIClient()
        client.post("/api/user/", newUser, format="json")
        response = client.put("/api/user/1/", updateUser, format="json")
        self.assertEqual(status.HTTP_200_OK, response.status_code)

    def testShouldGetUser(self):
        client = APIClient()
        client.post("/api/user/", newUser, format="json")
        response = client.get("/api/user/")
        self.assertEqual(getUser.get("name"), response.data[0]["name"])

    def testShouldDeleteUser(self):
        client = APIClient()
        client.post("/api/user/", newUser, format="json")
        response = client.delete("/api/user/1/")
        self.assertEqual(status.HTTP_204_NO_CONTENT, response.status_code)

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
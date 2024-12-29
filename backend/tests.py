from django.test import TestCase, Client
from django.urls import reverse
from rest_framework.test import APIRequestFactory

from .models import User, Order
from .serializers import UserSerializer

class ModelTestCase(TestCase):
    def test_user_creation(self):
        user = User.objects.create(email="test@example.com", password="testpassword")
        self.assertEqual(user.email, "test@example.com")

    def test_order_creation(self):
        user = User.objects.create(email="test@example.com", password="testpassword")
        order = Order.objects.create(user=user, total_sum=100)
        self.assertEqual(order.total_sum, 100)


class ViewTestCase(TestCase):
    def test_user_registration(self):
        client = Client()
        response = client.post(reverse('register'), data={'email': 'test@example.com', 'password': 'testpassword'})
        self.assertEqual(response.status_code, 201)
        self.assertTrue(User.objects.filter(email='test@example.com').exists())


class SerializerTestCase(TestCase):
    def test_user_serializer(self):
        user = User.objects.create(email="test@example.com", password="testpassword")
        factory = APIRequestFactory()
        request = factory.get('/users/')
        serializer = UserSerializer(user, context={'request': request})
        self.assertIn('email', serializer.data)
        self.assertEqual(serializer.data['email'], 'test@example.com')
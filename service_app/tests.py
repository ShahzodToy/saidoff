from django.test import TestCase
from rest_framework.test import APITestCase
from .models import Service,ServiceDescription,Order,Portfolio
from .api.serializers import ServiceSerializer, ServiceDescriptionSerializer, OrderSerializer, PortfolioSerializer


class ServiceTestCase(APITestCase):
    def setUp(self):
        self.service = Service.objects.create(
            title = 'test1'
        )

        self.service_desc = ServiceDescription.objects.create(
            service = self.service,
            title = 'test2',
            description = 'test2',
            image = 'test1.png'
        )

        self.order = Order.objects.create(
            name  = 'Shahzod',
            phone_number = '+99894933322',
            service_name = self.service,
            message = 'test1',
            is_checked = False
        )


    def test_service(self):
        serializer = ServiceDescriptionSerializer(self.service_desc)
        serializer_data = serializer.data

        self.assertEqual(serializer_data['title'],'test2')
        self.assertEqual(serializer_data['service'],self.service.id)
        self.assertEqual(serializer_data['description'],'test2')
        self.assertEqual(serializer_data['image'],'/media/test1.png')

    def test_order_service(self):
        serializer = OrderSerializer(self.order)
        serializer_data = serializer.data

        self.assertEqual(serializer_data['name'],'Shahzod')
        self.assertEqual(serializer_data['service_name'],self.service.id)
        self.assertEqual(serializer_data['phone_number'],'+99894933322')
        self.assertFalse(serializer_data['is_checked'])
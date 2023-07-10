from rest_framework.test import APITestCase

from main.models import Crosses
from main.serializers import CrossModelSerializer


class TestSerializers(APITestCase):

    def test_cross_serializer(self):
        cross1 = Crosses.objects.create(title="New balance", description="Good", price=1200)
        cross2 = Crosses.objects.create(title="Adidas", description="Excelent", price=2000)
        expected_data = [
        {
            'id': cross1.id,
            "title": "New balance",
            "get_factory_name": None,
            "factory": None,
            'description': 'Good',
            'price': '1200.00',
        },
        {
            'id': cross2.id,
            "title": "Adidas",
            "get_factory_name": None,
            "factory": None,
            'description': 'Excelent',
            'price': '2000.00',
        },
        ]
        self.assertEqual(expected_data, CrossModelSerializer([cross1, cross2], many=True).data)
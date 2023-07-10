from rest_framework.reverse import reverse
from rest_framework.test import APITestCase

from main.models import Crosses
from main.serializers import CrossModelSerializer


class CrossModelViewSetTest(APITestCase):

    def test_cross_model_list(self):
        url = reverse("modelviewset_croses")
        print(url)
        cross1 = Crosses.objects.create(title="New balance", description="Good", price=1200)
        cross2 = Crosses.objects.create(title="Adidas", description="Excelent", price=2000)

        response = self.client.get("http://127.0.0.1:8000/api/v1/main/modelviewset_croses/")
        serializer = CrossModelSerializer([cross1, cross2], many=True).data
        self.assertEqual(200, response.status_code)
        self.assertEqual(serializer, response.data.get('results'))

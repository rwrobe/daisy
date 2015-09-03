import unittest
from mock import Mock
from rest_framework.test import APIRequestFactory, APIClient, force_authenticate
from risks.models import Risk
from authentication.models import Account
from risks.serializers import RiskSerializer
from risks.views import RiskViewSet


class RiskTest(unittest.TestCase):

    def setUp(self):
        self.account = Mock(spec=Account, id=1,username='johndoe')
        self.account._state = Mock()

    def testRiskUnicode(self):
        risk = Risk(id=1,user=self.account,code=23, duration=12)
        risk = str(risk)

        self.assertEqual(risk, '23 12')

class RiskSerializerTest(unittest.TestCase):

    def setUp(self):
        self.account = Mock(spec=Account, id=1,username='johndoe', email='test@test.is')
        self.account._state = Mock()
        self.risk = Mock(spec=Risk,id=1,user=self.account,code=23, duration=12)

    def testRiskSerializer(self):
        serialized_risk = RiskSerializer(self.risk)
        self.assertEqual(str(serialized_risk.data), "{'duration': 12, 'code': 23, 'id': 1, 'user': OrderedDict([('id', 1), ('email', u'test@test.is'), ('username', u'johndoe')])}")

# @see http://www.django-rest-framework.org/api-guide/testing/
class RiskViewSetTest(unittest.TestCase):

    def setUp(self):
        pass

    #def testPostSuccess(self):
        #account = Account.objects.get(username='wardrobe')
        #factory = APIRequestFactory()
        #request = factory.put('/api/v1/risks/',{'code': 22, 'duration': 22}, format='json')
        #force_authenticate(request, user=account)
        #response = view(request)
        #self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def testClientView(self):
        client = APIClient()
        client.login(username='wardrobe',password='balmer411')
        response = APIClient().get('/api/v1/risks/')
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
import unittest
from mock import Mock
from rest_framework.test import APIRequestFactory, APIClient, force_authenticate
from risks.models import Risk
from authentication.models import Account, AccountManager
from risks.serializers import RiskSerializer


class RiskTest(unittest.TestCase):

    def setUp(self):
        self.account = Account.objects.create(email='this@email.com', username='this', password='73s47')

    def testRiskUnicode(self):
        risk = Risk.objects.create(user=self.account,code=23, duration=12)
        risk = str(risk)

        self.assertEqual(risk, '23 12')


class RiskSerializerTest(unittest.TestCase):

    def setUp(self):
        self.account = Account.objects.create(email='another@email.com', username='another', password='73s47')
        self.risk = Risk.objects.create(user=self.account, code='111', duration='111')

    def testRiskSerializer(self):
        serialized_risk = RiskSerializer(self.risk)
        '''
         Can't compare the whole dump, because the time stamps will constantly change, so I'm going to split the string.
        '''
        risk_dict = str(serialized_risk.data).split()
        self.assertEqual( risk_dict[1], "111,") # code test
        self.assertEqual( risk_dict[10], "u'another@email.com'),") # email of the user
        self.assertEqual( risk_dict[12], "u'another'),") # email of the user


# @see http://www.django-rest-framework.org/api-guide/testing/
class RiskViewSetTest(unittest.TestCase):

    def setUp(self):
        self.client = APIClient(enforce_csrf_checks=True)
        self.account = Account.objects.create_superuser(email='evenmore@email.com', username='evenmore', password='73s47')

    def testClientView(self):
        self.client.login(username='evenmore@email.com',password='73s47')
        response = self.client.get('/api/v1/risks/')
        self.assertTrue(response.status_code, 200)

    #def testRequestView(self):
        #view = RiskSerializer.as_view({'get':'list'})
        #factory = APIRequestFactory()
        #request = factory.post('/api/v1/risks/',{'code':101,'duration':101})
        #force_authenticate(request, user=self.user)
        #response = view(request)
        #pass

if __name__ == '__main__':
    unittest.main()
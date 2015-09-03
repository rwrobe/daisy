from authentication.models import Account, AccountManager
from mock import MagicMock
import unittest


class AccountTest(unittest.TestCase):

    def setUp(self):
        self.tAccount = Account(email='test@test.is',username='testy',first_name='testy',last_name="mctesterson")

    def testAccountEmail(self):
        self.assertEqual(self.tAccount.email, 'test@test.is')
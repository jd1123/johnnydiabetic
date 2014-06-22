from django.test import TestCase
from basefunctions.models import UserProfile
from django.contrib.auth.models import User

# Create your tests here.

class UserProfileTestCase(TestCase):
    def setUp(self):
        user = User.objects.create_user(username = 'nancy',
                                        password = 'opensesame',
                                        email = 'nancy@nancy.com')
        user.save()
        UserProfile.objects.create(user=user, website="http://www.johnnydiabetic.com")

    def test_creation(self):
        pfl = UserProfile.objects.all()
        self.assertFalse(pfl[0]==None, "UserProfile was not successfully created")

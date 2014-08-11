from django.test import TestCase
from basefunctions.models import UserProfile
from django.contrib.auth.models import User
from basefunctions.templatetags import custom_tags
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


class TestCustomTags(TestCase):
    def setUp(self):
        pass

    def test_secure_file_gallery(self):
        path = '/protected'
        filename = 'pic.jpg'
        gallery = 'wedding'
        context = {'user_authenticated':True}
        p = custom_tags.secure_file(context,filename, None, None, gallery)
        self.assertEqual(p, '<img src=\'/file/wedding/pic.jpg\'>', \
                         'the path should be <img src=\'/file/wedding/pic.jpg\'> it is : ' + p)

    def test_secure_file_path(self):
        path = '/protected'
        filename = 'pic.jpg'
        gallery = None
        context = {'user_authenticated':True}
        p = custom_tags.secure_file(context,filename, None, None, gallery)
        self.assertEqual(p, '<img src=\'/file/pic.jpg\'>', \
                         'the path should be <img src=\'/file/pic.jpg\'> it is : ' + p)



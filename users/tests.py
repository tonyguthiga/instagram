from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from django.contrib.auth.models import User
from .models import Profile


class ProfileTestClass(TestCase):
    '''
    test class for Profile model
    '''
    def setUp(self):
        self.user = User.objects.create_user("testuser", "secret")
        self.profile_test = Profile(image='https://ucarecdn.com/620ac26e-19f7-4c0a-86d1-2b4e4b195fa8/-/crop/610x452/15,0/-/preview/',
                                    bio="this is a test bio",
                                    owner=self.user)
        self.profile_test.save()

    def test_instance_true(self):
        self.profile_test.save()
        self.assertTrue(isinstance(self.profile_test, Profile))
from django.test import TestCase, Client, tag
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model,authenticate
from .models import contact_model
from unittest import mock
from django.urls import reverse
from django.core.files import File
from accounts.models import User
#Profile App test:
@tag('unit-test')
class ProfileAppsTestCase(TestCase):
    def test_apps_name(self):
        self.assertEqual(ProfileConfig.name, "profile")





class MyProfileTest(TestCase):
    def setUp(self):
        #Arrange
        self.user = User.objects.create(email='testmy_profileTest@text.com',
                                        user_name='my_profileTest user name',
                                        first_name='first name',
                                        last_name='last name',
                                        about='This is test',
                                        profile_image=None)
        self.user.set_password('user password')
        self.user.save()

    @tag('unit-test')
    def test_view_url(self):
        #Arrange
        self.client.force_login(self.user)

        #Act
        response = self.client.get(reverse('Profile:my_profile'))

        #Assert
        self.assertEqual(response.status_code, 200)

    @tag('unit-test')
    def test_view_uses_correct_template(self):
        #Arrange
        self.client.force_login(self.user)

        #Act
        response = self.client.get(reverse('Profile:my_profile'))

        #Assert
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'Profile/my_profile.html')

from django.test import TestCase, Client, tag
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model,authenticate
from .models import contact_model,User,Manager,Parent,Video,Gallery
from .apps import UsersConfig
from .forms import ManagerForm,Gallery_form,Video_form
from django.core.files.uploadedfile import SimpleUploadedFile


@tag('unit-test')
class VideoModelTestModel(TestCase):
    def setUp(self):
        self.model = Video.objects.create(caption= 'ss',
                                            video= '',
                                            gangrp='12')
    def test_maxlen_caption(self):
        max_length = self.model._meta.get_field('caption').max_length
        self.assertEqual(max_length, 100)

    def test_group(self):
        max_length = self.model._meta.get_field('gangrp').max_length
        self.assertEqual(max_length, 100)

@tag('unit-test')
class GalleryTestModel(TestCase):
    def setUp(self):
        self.model = Gallery.objects.create(caption= 'ss',
                                            picture= '',
                                            gangrp='12')
    def test_maxlen_caption(self):
        max_length = self.model._meta.get_field('caption').max_length
        self.assertEqual(max_length, 100)

    def test_group(self):
        max_length = self.model._meta.get_field('gangrp').max_length
        self.assertEqual(max_length, 100)
# Tests For video and pictures - Problem Permission dine
# @tag('unit-test')
# class GalleryTestForm(TestCase):
#     def setUp(self):
#         form_data = {'caption': 'ss',
#                     'picture': '',
#                     'gangrp':'12'}
#         self.form = Gallery_form(form_data)
#     def test_upload_pictures(self):
#         self.form.picture = SimpleUploadedFile(name='test_image.jpg', content=open('media', 'rb').write(), content_type='image/jpeg')
#         self.assertTrue(self.model.picture.is_valid())
# class VideoTestForm(TestCase):
#     def setUp(self):
#         form_data = {'caption': 'ss',
#                     'video': '',
#                     'gangrp':'12'}
#         self.form = Video_form(form_data)
#     def test_upload_Video(self):
#         self.form.picture = SimpleUploadedFile(name='test_image.jpg', content=open('media', 'rb').write(), content_type='image/jpeg')
#         self.assertTrue(self.model.picture.is_valid())

@tag('unit-test')
class ProfileAppsTestCase(TestCase):
    def test_apps_name(self):
        self.assertEqual(UsersConfig.name, "users")

#Test For Manager Forms
@tag('unit-test')
class ManagerFormTest(TestCase):
    def setUp(self):
        form_data = {'email': 'test@text.com',
                     'phone_number':'0522222222',
                     'first_name': 'first name',
                     'last_name': 'last name',
                     }
        self.form = ManagerForm(data=form_data)

    def test_first_name_label(self):
        self.assertFalse(self.form.fields['first_name'].label, 'first_name')
    def test_first_name_required(self):
        self.assertTrue(self.form.fields['first_name'].required)

    def test_last_name_label(self):
        self.assertFalse(self.form.fields['last_name'].label, 'last_name')

    def test_last_name_required(self):
        self.assertTrue(self.form.fields['last_name'].required)

    def test_phoneNumber_lable(self):
        self.assertFalse(self.form.fields['phone_number'].label, 'phone_number')

    def test_phoneNumber_required(self):
        self.assertTrue(self.form.fields['phone_number'].required)

    def test_valid_form(self):
        self.assertFalse(self.form.is_valid())


#Test For Parents Forms
@tag('unit-test')
class ParentsFormTest(TestCase):
    def setUp(self):
        form_data = {'phone_number':'0522222222',
                     'first_name': 'first name',
                     'last_name': 'last name',
                     }
        self.form = ManagerForm(data=form_data)

    def test_first_name_label(self):
        self.assertFalse(self.form.fields['first_name'].label, 'first_name')

    def test_first_name_required(self):
        self.assertTrue(self.form.fields['first_name'].required)

    def test_last_name_label(self):
        self.assertFalse(self.form.fields['last_name'].label, 'last_name')

    def test_last_name_required(self):
        self.assertTrue(self.form.fields['last_name'].required)

    def test_phoneNumber_lable(self):
        self.assertFalse(self.form.fields['phone_number'].label, 'phone_number')

    def test_phoneNumber_required(self):
        self.assertTrue(self.form.fields['phone_number'].required)

    def test_valid_form(self):
        self.assertFalse(self.form.is_valid())


@tag('unit-test')
class TestAdminPanel(TestCase):
    def create_user(self):
        self.username = "test_admin"
        self.password = '12GooGle12'
        user, created = User.objects.get_or_create(username=self.username)
        user.set_password(self.password)
        user.is_staff = True
        user.is_superuser = True
        user.is_active = True
        user.save()
        self.user = user

    def test_spider_admin(self):
        self.create_user()
        client = Client()
        client.login(username=self.username, password=self.password)
        admin_pages = [
            "/admin/",
            "/admin/auth/",
            "/admin/auth/group/",
            "/admin/auth/group/add/",
            "/admin/auth/user/",
            "/admin/auth/user/add/",
            "/admin/password_change/"
        ]
        # for page in admin_pages:
        #     resp = client.get(page)
        #     self.assertFalse(resp,'200')
            #assert "<!DOCTYPE html" in resp.content

from django.test import TestCase, tag
from django.urls import resolve, reverse
from users.views import index, regpage

@tag('unit-test')
class UrlsTest(TestCase):
    def test_sign_up_url_resolved(self):
        #Act
        url = reverse('homepage')
        #Assert
        self.assertEqual(resolve(url).func, index)

@tag('unit-test')
class SigninTest(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(username='test', password='12test12', email='test@example.com')
        self.user.save()

    def tearDown(self):
        self.user.delete()

    def test_correct(self):
        user = authenticate(username='test', password='12test12')
        self.assertTrue((user is not None) and user.is_authenticated)

    def test_wrong_username(self):
        user = authenticate(username='wrong', password='12test12')
        self.assertFalse(user is not None and user.is_authenticated)

    def test_wrong_pssword(self):
        user = authenticate(username='test', password='wrong')
        self.assertFalse(user is not None and user.is_authenticated)


@tag('unit-test')
class contactTest(TestCase):

    def setUp(self):
        self.contact = contact_model.objects.create(parent_name='parent',
                                    child_name='child',phone_number=1234567890,
                                    email="test@gmail.com")
        self.contact.save()

    def tearDown(self):
        self.contact.delete()

    def test_exists(self):
        obj = contact_model.objects.get(parent_name='parent')
        self.assertTrue(self.contact is not None)

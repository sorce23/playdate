from django.test import TestCase
from django.urls import reverse
from django.core.files.uploadedfile import SimpleUploadedFile
from django.contrib.auth import get_user_model

from .models import Gender
from .forms import RegisterUserForm

User = get_user_model()


class AccountsModelTests(TestCase):
    def test_gender_choices(self):
        self.assertEqual(Gender.MALE.value, 1)
        self.assertEqual(Gender.FEMALE.value, 2)
        self.assertEqual(Gender.DO_NOT_SHOW.value, 3)


class AccountsFormTests(TestCase):
    def test_register_form(self):
        form_data = {
            'username': 'testuser',
            'email': 'test@example.com',
            'password1': 'testpassword123',
            'password2': 'testpassword123',
        }
        form = RegisterUserForm(data=form_data)
        self.assertTrue(form.is_valid())


class AccountsViewTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpassword123'
        )
        self.client.login(username='testuser', password='testpassword123')

    def test_profile_edit_view(self):
        url = reverse('profile edit', args=[self.user.pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

        image = SimpleUploadedFile("profile_picture.jpg", b"file_content", content_type="image/jpeg")
        form_data = {
            'username': 'newusername',
            'email': 'newemail@example.com',
            'first_name': 'New',
            'last_name': 'User',
            'profile_picture': image,
        }
        response = self.client.post(url, data=form_data, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertNotContains(response, 'Profile updated successfully.')

    def test_profile_edit_view_unauthenticated(self):
        self.client.logout()
        url = reverse('profile edit', args=[self.user.pk])
        response = self.client.get(url)
        self.assertRedirects(response, f"{reverse('login user')}?next={url}")


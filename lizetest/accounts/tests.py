from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

class SignUpViewTests(TestCase):
    def setUp(self):
        self.url = reverse('accounts:signup')
        self.login_url = reverse('todo:task_list')  
        self.user_model = get_user_model()

    def test_form_valid(self):
        """
        Test the behavior of the SignUpView with a valid form submission.
        """
        form_data = {
            'username': 'newuser',
            'email': 'newuser@example.com',
            'password1': 'testpassword123',
            'password2': 'testpassword123',
        }
        response = self.client.post(self.url, form_data)
        self.assertEqual(response.status_code, 302)  # Espera-se um redirecionamento após o sucesso
        self.assertTrue(self.user_model.objects.filter(username='newuser').exists())

    def test_form_invalid(self):
        """
        Test the behavior of the SignUpView with an invalid form submission.
        """
        form_data = {
            'username': 'newuser',
            'email': 'newuser@example.com',
            'password1': 'testpassword123',
            'password2': 'wrongpassword',
        }
        response = self.client.post(self.url, form_data)
        self.assertEqual(response.status_code, 200)  # Permanece na mesma página
        self.assertFalse(self.user_model.objects.filter(username='newuser').exists())
        self.assertFormError(response, 'form', 'password2', "Os dois campos de senha não correspondem.")

    def test_form_empty_submission(self):
        """
        Test the behavior when submitting an empty form.
        """
        form_data = {}
        response = self.client.post(self.url, form_data)
        self.assertEqual(response.status_code, 200)  # Permanece na mesma página
        self.assertIn('Este campo é obrigatório.', response.content.decode())

    def test_successful_signup_redirect(self):
        """
        Test that a successful signup redirects the user to the login page.
        """
        form_data = {
            'username': 'validuser',
            'email': 'validuser@example.com',
            'password1': 'ValidPassword123!',
            'password2': 'ValidPassword123!',
        }
        response = self.client.post(self.url, form_data, follow=True)
        self.assertRedirects(response, self.login_url)
        self.assertTrue(self.user_model.objects.filter(username='validuser').exists())

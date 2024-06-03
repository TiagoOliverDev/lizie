from django.http import HttpResponse
from django.urls import reverse_lazy
from django.contrib.auth import login
from django.views.generic.edit import FormView

from .forms import CustomUserCreationForm
from .models import User

import logging

logger = logging.getLogger(__name__)

class SignUpView(FormView):
    """
    View for handling user sign-up process using a custom user creation form.
    """
    model = User
    form_class = CustomUserCreationForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('todo:task_list')

    def form_valid(self, form: CustomUserCreationForm) -> HttpResponse:
        """
        Process the form when it is valid. Registers a new user and logs them in.

        Args:
            form (CustomUserCreationForm): The form filled out by the user.

        Returns:
            HttpResponse: Redirects the user to the success URL upon successful registration.
        """
        try:
            user = form.save()
            logger.info(f"User {user} created successfully")
            login(self.request, user) 
        except Exception as e:
            logger.error(f"Failed to create and login user: {e}")
            return self.form_invalid(form)

        return super().form_valid(form)

    def form_invalid(self, form: CustomUserCreationForm) -> HttpResponse:
        """
        Handle the scenario when the form is invalid. Logs errors and provides feedback.

        Args:
            form (CustomUserCreationForm): The form containing errors.

        Returns:
            HttpResponse: Renders the form with validation errors.
        """
        logger.error("Form is invalid")
        logger.error(form.errors)
        return super().form_invalid(form)

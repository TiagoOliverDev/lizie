import logging
from django.urls import reverse_lazy
from django.contrib.auth import login
from django.views.generic.edit import FormView
from .forms import CustomUserCreationForm
from .models import User

logger = logging.getLogger(__name__)

class SignUpView(FormView):
    model = User
    form_class = CustomUserCreationForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('accounts:login')

    def form_valid(self, form):
        logger.info("Form is valid")
        user = form.save()
        logger.info(f"User {user} created successfully")
        login(self.request, user)
        return super().form_valid(form)

    def form_invalid(self, form):
        logger.error("Form is invalid")
        logger.error(form.errors)
        return super().form_invalid(form)

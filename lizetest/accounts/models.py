from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, UserManager, PermissionsMixin

# Create your models here.
class User(AbstractBaseUser, PermissionsMixin):
	username = models.CharField(
		_('username'),
		max_length=150,
		unique=True,
		help_text=('150 caracteres ou menos. Letras, números e @/./+/-/_ apenas.'),
		error_messages={
			'unique': _("A user with that username already exists."),
		},
		null=True,
		blank=True
	)
	name = models.CharField(_('name'), max_length=100, blank=True)
	email = models.EmailField(_('email address'), unique=True)
	is_staff = models.BooleanField(
		_('staff status'),
		default=False,
		help_text=_('Designates whether the user can log into this admin site.'),
	)
	
	is_active = models.BooleanField(
		_('active'),
		default=True,
		help_text=_(
			'Designates whether this user should be treated as active. '
			'Unselect this instead of deleting accounts.'
		),
	)

	objects = UserManager()

	EMAIL_FIELD = 'email'
	USERNAME_FIELD = 'username'
	REQUIRED_FIELDS = ['email']

	class Meta:
		verbose_name = 'usuário'
		verbose_name_plural = 'usuários'

	def __str__(self):
		return self.name or self.username or self.email

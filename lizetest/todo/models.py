# models.py
from django.db import models
from django.conf import settings

from lizetest.core.models import BaseModel


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Task(BaseModel):
    title = models.CharField(max_length=255)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    completion_date = models.DateTimeField(null=True, blank=True)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title
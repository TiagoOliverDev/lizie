from django import forms
from .models import Task
from .models import Category

class TaskForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super(TaskForm, self).__init__(*args, **kwargs)
        if user:
            self.fields['category'].queryset = Category.objects.filter(user=user)

    class Meta:
        model = Task
        fields = ['title', 'description', 'category']
class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']

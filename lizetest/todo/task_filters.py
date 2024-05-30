import django_filters
from .models import Task, Category

class TaskFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains')
    category = django_filters.ModelChoiceFilter(queryset=Category.objects.none())

    class Meta:
        model = Task
        fields = ['title', 'category']

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super(TaskFilter, self).__init__(*args, **kwargs)
        if user:
            self.filters['category'].queryset = Category.objects.filter(user=user)

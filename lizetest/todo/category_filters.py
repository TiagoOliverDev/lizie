import django_filters
from .models import Category

class CategoryFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Category
        fields = ['name']

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super(CategoryFilter, self).__init__(*args, **kwargs)
        if user:
            self.queryset = Category.objects.filter(user=user)

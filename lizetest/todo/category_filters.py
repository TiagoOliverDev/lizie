import django_filters
from .models import Category
import logging

logger = logging.getLogger(__name__)

class CategoryFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains', label='Search by category name')

    class Meta:
        model = Category
        fields = ['name']

    def __init__(self, *args, **kwargs):
        """
        Initializes the filter set with a queryset filtered by the user.
        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments. Expects 'user' to specify the owner of the categories.

        Raises:
            ValueError: If 'user' is not provided in kwargs, though continues with default queryset.
        """
        user = kwargs.pop('user', None)
        try:
            super(CategoryFilter, self).__init__(*args, **kwargs)
            if user is not None:
                self.queryset = Category.objects.filter(user=user)
            else:
                raise ValueError("User must be provided to initialize CategoryFilter")
        except Exception as e:
            logger.error(f"An error occurred while initializing the CategoryFilter: {e}")
            raise ValueError(f"An error occurred while initializing the CategoryFilter: {e}")

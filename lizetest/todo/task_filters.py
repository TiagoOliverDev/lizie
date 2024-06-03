import logging
import django_filters
from .models import Task, Category

logger = logging.getLogger(__name__)

class TaskFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains', label='Search tasks by title')
    category = django_filters.ModelChoiceFilter(queryset=Category.objects.none(), label='Filter by category')

    class Meta:
        model = Task
        fields = ['title', 'category']

    def __init__(self, *args, **kwargs):
        """
        Initializes the filter with a user-specific category queryset.
        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments, expects 'user' to filter categories.

        Raises:
            ValueError: If 'user' is not provided, it raises a ValueError.
        """
        user = kwargs.pop('user', None)
        try:
            super(TaskFilter, self).__init__(*args, **kwargs)
            if user is not None:
                self.filters['category'].queryset = Category.objects.filter(user=user)
            else:
                raise ValueError("User must be provided to initialize TaskFilter")
        except Exception as e:
            logger.error(f"Failed to initialize TaskFilter: {e}")
            raise ValueError(f"Failed to initialize TaskFilter: {e}")

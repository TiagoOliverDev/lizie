from django.urls import reverse_lazy
from django.db.models import QuerySet
from django.views.generic import CreateView, DeleteView, UpdateView
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.http import HttpResponse, HttpResponseForbidden

from .models import Category
from .forms import CategoryForm
from .category_filters import CategoryFilter
from django_filters.views import FilterView

import logging

logger = logging.getLogger(__name__)

class CategoryListView(LoginRequiredMixin, FilterView):
    model = Category
    filterset_class = CategoryFilter
    template_name = 'category_list.html'
    context_object_name = 'categories'

    def get_queryset(self) -> 'QuerySet[Category]':
        """Returns queryset of categories owned by the logged-in user."""
        try:
            return Category.objects.filter(user=self.request.user)
        except Exception as e:
            logger.error(f"Error retrieving categories: {e}")
            raise HttpResponseForbidden(f"Error retrieving categories: {e}")

    def get_filterset_kwargs(self, filterset_class) -> dict:
        """Provides user-specific kwargs to the filterset."""
        try:
            kwargs = super(CategoryListView, self).get_filterset_kwargs(filterset_class)
            kwargs['user'] = self.request.user
            return kwargs
        except Exception as e:
            logger.error(f"Error setting filter parameters: {e}")
            raise HttpResponseForbidden(f"Error setting filter parameters: {e}")

class CategoryCreateView(LoginRequiredMixin, CreateView):
    model = Category
    form_class = CategoryForm
    template_name = 'category_form.html'
    success_url = reverse_lazy('todo:category_list')

    def form_valid(self, form) -> HttpResponse:
        """Sets the category user before saving the form."""
        form.instance.user = self.request.user
        try:
            return super(CategoryCreateView, self).form_valid(form)
        except Exception as e:
            logger.error(f"Failed to save category: {e}")
            form.add_error(None, f"Failed to save category: {e}")
            return self.form_invalid(form)

class CategoryUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Category
    form_class = CategoryForm
    template_name = 'category_form.html'
    success_url = reverse_lazy('todo:category_list')

    def test_func(self) -> bool:
        """Ensures only the owner of the category can update it."""
        try:
            return self.get_object().user == self.request.user
        except Category.DoesNotExist:
            return False

    def form_valid(self, form) -> HttpResponse:
        """Updates category data if the current user is the owner."""
        if not self.test_func():
            return HttpResponseForbidden("Unauthorized attempt to update category.")
        try:
            return super(CategoryUpdateView, self).form_valid(form)
        except Exception as e:
            logger.error(f"Failed to update category: {e}")
            form.add_error(None, f"Failed to update category: {e}")
            return self.form_invalid(form)

class CategoryDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Category
    template_name = 'category_confirm_delete.html'
    success_url = reverse_lazy('todo:category_list')

    def test_func(self) -> bool:
        """Ensures only the owner of the category can delete it."""
        try:
            return self.get_object().user == self.request.user
        except Category.DoesNotExist:
            return False

    def delete(self, request, *args, **kwargs) -> HttpResponse:
        """Deletes category if the current user is the owner."""
        if not self.test_func():
            logger.info("Unauthorized attempt to delete category.")
            return HttpResponseForbidden("Unauthorized attempt to delete category.")
        try:
            return super(CategoryDeleteView, self).delete(request, *args, **kwargs)
        except Exception as e:
            logger.error(f"Failed to delete category: {e}")
            return HttpResponseForbidden(f"Failed to delete category: {e}")

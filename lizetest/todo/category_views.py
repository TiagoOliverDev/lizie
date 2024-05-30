from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Category
from .forms import CategoryForm
from .category_filters import CategoryFilter
from django_filters.views import FilterView


class CategoryListView(LoginRequiredMixin, FilterView):
    model = Category
    filterset_class = CategoryFilter
    template_name = 'category_list.html'
    context_object_name = 'categories'

    def get_queryset(self):
        return Category.objects.filter(user=self.request.user)

    def get_filterset_kwargs(self, filterset_class):
        kwargs = super(CategoryListView, self).get_filterset_kwargs(filterset_class)
        kwargs['user'] = self.request.user
        return kwargs

class CategoryCreateView(LoginRequiredMixin, CreateView):
    model = Category
    form_class = CategoryForm
    template_name = 'category_form.html'
    success_url = reverse_lazy('todo:category_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(CategoryCreateView, self).form_valid(form)

class CategoryUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Category
    form_class = CategoryForm
    template_name = 'category_form.html'
    success_url = reverse_lazy('todo:category_list')

    def test_func(self):
        return self.get_object().user == self.request.user

class CategoryDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Category
    template_name = 'category_confirm_delete.html'
    success_url = reverse_lazy('todo:category_list')

    def test_func(self):
        return self.get_object().user == self.request.user

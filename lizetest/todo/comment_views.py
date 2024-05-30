from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Task, Category, Comment
from .forms import TaskForm, CategoryForm, CommentForm

class CommentUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Comment
    form_class = CommentForm
    template_name = 'comment_form.html'
    
    def get_success_url(self):
        return reverse_lazy('todo:task_details', kwargs={'pk': self.object.task.pk})

    def test_func(self):
        comment = self.get_object()
        return self.request.user == comment.user

class CommentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Comment
    template_name = 'comment_confirm_delete.html'
    
    def get_success_url(self):
        return reverse_lazy('todo:task_details', kwargs={'pk': self.object.task.pk})

    def test_func(self):
        comment = self.get_object()
        return self.request.user == comment.user

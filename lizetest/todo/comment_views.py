import logging
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import HttpResponseForbidden, HttpResponse

from .models import Comment
from .forms import CommentForm

logger = logging.getLogger(__name__)

class CommentUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Comment
    form_class = CommentForm
    template_name = 'comment_form.html'
    
    def get_success_url(self) -> str:
        """Returns the URL to redirect to after a successful update."""
        return reverse_lazy('todo:task_details', kwargs={'pk': self.object.task.pk})

    def test_func(self) -> bool:
        """Ensures that only the user who created the comment can update it."""
        comment = self.get_object()
        is_owner = self.request.user == comment.user
        if not is_owner:
            logger.warning(f"Unauthorized attempt to update comment by user {self.request.user.id}")
        return is_owner

    def form_valid(self, form) -> HttpResponse:
        """Processes the valid form; logs and handles errors."""
        try:
            return super(CommentUpdateView, self).form_valid(form)
        except Exception as e:
            logger.error(f"Error updating comment: {e}")
            form.add_error(None, f"Failed to update comment: {e}")
            return self.form_invalid(form)

class CommentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Comment
    template_name = 'comment_confirm_delete.html'
    
    def get_success_url(self) -> str:
        """Returns the URL to redirect to after successfully deleting a comment."""
        return reverse_lazy('todo:task_details', kwargs={'pk': self.object.task.pk})

    def test_func(self) -> bool:
        """Ensures that only the user who created the comment can delete it."""
        comment = self.get_object()
        is_owner = self.request.user == comment.user
        if not is_owner:
            logger.warning(f"Unauthorized attempt to delete comment by user {self.request.user.id}")
        return is_owner

    def delete(self, request, *args, **kwargs) -> HttpResponse:
        """Handles the comment deletion; logs errors if deletion fails."""
        if not self.test_func():
            logger.error("Unauthorized attempt to delete comment.")
            return HttpResponseForbidden("Unauthorized attempt to delete comment.")
        try:
            return super(CommentDeleteView, self).delete(request, *args, **kwargs)
        except Exception as e:
            logger.error(f"Failed to delete comment: {e}")
            return HttpResponseForbidden(f"Failed to delete comment: {e}")

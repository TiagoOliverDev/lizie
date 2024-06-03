from django.db.models import QuerySet
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.http import HttpResponse, HttpResponseForbidden
from django_filters.views import FilterView
from django.views.generic import ListView
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.lib import colors

from .models import Task
from .forms import TaskForm, CommentForm
from .task_filters import TaskFilter

import logging

logger = logging.getLogger(__name__)

class TaskListView(LoginRequiredMixin, FilterView):
    model = Task
    filterset_class = TaskFilter
    template_name = 'task_list.html'
    context_object_name = 'tasks'
    paginate_by = 7

    def get_queryset(self) -> 'QuerySet[Task]':
        """Filters tasks by the logged-in user with error handling."""
        try:
            return Task.objects.filter(user=self.request.user)
        except Exception as e:
            logger.error(f"Error retrieving tasks: {e}")
            raise HttpResponseForbidden(f"Error retrieving tasks: {e}")

    def get_filterset_kwargs(self, filterset_class) -> dict:
        """Injects user into filterset kwargs for user-specific filtering with error handling."""
        try:
            kwargs = super(TaskListView, self).get_filterset_kwargs(filterset_class)
            kwargs['user'] = self.request.user
            return kwargs
        except Exception as e:
            logger.error(f"Error configuring filter: {e}")
            raise HttpResponseForbidden(f"Error configuring filter: {e}")

class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Task
    form_class = TaskForm
    template_name = 'task_form.html'
    success_url = reverse_lazy('todo:task_list')

    def get_form_kwargs(self) -> dict:
        """Provides user instance to form for processing with error handling."""
        try:
            kwargs = super(TaskCreateView, self).get_form_kwargs()
            kwargs['user'] = self.request.user
            return kwargs
        except Exception as e:
            logger.error(f"Error accessing form data: {e}")
            raise HttpResponseForbidden(f"Error accessing form data: {e}")

    def form_valid(self, form) -> HttpResponse:
        """Assigns task to user before saving with error handling."""
        try:
            form.instance.user = self.request.user
            return super(TaskCreateView, self).form_valid(form)
        except Exception as e:
            logger.error(f"Error saving task: {e}")
            form.add_error(None, f"Error saving task: {e}")
            return self.form_invalid(form)

class TaskDetailView(LoginRequiredMixin, DetailView):
    model = Task
    template_name = 'task_details.html'
    context_object_name = 'task'

    def get_context_data(self, **kwargs) -> dict:
        """Adds comments and a comment form to the template context with error handling."""
        try:
            context = super().get_context_data(**kwargs)
            context['comments'] = self.object.comments.all()
            context['comment_form'] = CommentForm()
            return context
        except Exception as e:
            logger.error(f"Error loading task details: {e}")
            return HttpResponseForbidden(f"Error loading task details: {e}")

    def post(self, request, *args, **kwargs) -> HttpResponse:
        """Handles posting a new comment to a task with error handling."""
        try:
            self.object = self.get_object()
            form = CommentForm(request.POST)
            if form.is_valid():
                comment = form.save(commit=False)
                comment.task = self.object
                comment.user = request.user
                comment.save()
                return redirect('todo:task_details', pk=self.object.pk)
            return self.render_to_response(self.get_context_data(form=form))
        except Exception as e:
            logger.error(f"Error processing comment: {e}")
            return HttpResponseForbidden(f"Error processing comment: {e}")

class TaskUpdateView(LoginRequiredMixin, UpdateView):
    model = Task
    form_class = TaskForm
    template_name = 'task_form.html'
    success_url = reverse_lazy('todo:task_list')

    def get_form_kwargs(self) -> dict:
        """Provides user instance to form for processing with error handling."""
        try:
            kwargs = super(TaskUpdateView, self).get_form_kwargs()
            kwargs['user'] = self.request.user
            return kwargs
        except Exception as e:
            logger.error(f"Error accessing form data: {e}")
            raise HttpResponseForbidden(f"Error accessing form data: {e}")

class TaskDeleteView(LoginRequiredMixin, DeleteView):
    model = Task
    template_name = 'task_confirm_delete.html'
    success_url = reverse_lazy('todo:task_list')

    def form_valid(self, form) -> HttpResponse:
        """Prevents deletion of completed tasks with error handling."""
        try:
            if self.object.completed:
                context = self.get_context_data()
                context['error'] = "Cannot delete a completed task."
                return self.render_to_response(context)
            return super().form_valid(form)
        except Exception as e:
            logger.error(f"Error during deletion process: {e}")
            return HttpResponseForbidden(f"Error during deletion process: {e}")

    def get_context_data(self, **kwargs) -> dict:
        """Adds completion status to the context with error handling."""
        try:
            context = super().get_context_data(**kwargs)
            context['is_completed'] = self.object.completed
            return context
        except Exception as e:
            logger.error(f"Error accessing task data: {e}")
            return HttpResponseForbidden(f"Error accessing task data: {e}")

class CompletedTasksListView(LoginRequiredMixin, ListView):
    """
    Displays a list of tasks that are marked as completed.
    """
    model = Task
    template_name = 'completed_tasks_list.html' 
    context_object_name = 'completed_tasks'
    paginate_by = 7 

    def get_queryset(self):
        """
        Return only the tasks that are marked as completed for the logged-in user.
        """
        return Task.objects.filter(user=self.request.user, completed=True)
    

def download_tasks_pdf(request):
    # Configuração de resposta HTTP para enviar arquivo PDF
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="completed_tasks.pdf"'

    # Cria um documento PDF e define seu título
    doc = SimpleDocTemplate(response, pagesize=letter)
    story = []

    # Consulta as tarefas completadas
    tasks = Task.objects.filter(user=request.user, completed=True).values('title', 'description', 'category__name')

    # Prepara dados para a tabela
    data = [['Title', 'Description', 'Category']]
    data += [[task['title'], task['description'], task['category__name']] for task in tasks]

    # Cria a tabela
    t = Table(data, splitByRow=1, repeatRows=1)

    # Adiciona estilos à tabela
    t.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.gray),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
    ]))

    # Adiciona a tabela ao story
    story.append(t)

    doc.build(story)
    return response
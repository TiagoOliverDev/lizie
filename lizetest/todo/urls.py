from django.urls import path
from .views import (TaskListView, TaskCreateView, TaskUpdateView, TaskDeleteView, TaskDetailView, CompletedTasksListView)
from .category_views import(CategoryListView, CategoryCreateView, CategoryUpdateView, CategoryDeleteView)
from .comment_views import (CommentUpdateView, CommentDeleteView)
from .api_view import (toggle_task_complete)

app_name = "todo"

urlpatterns = [
    path('', TaskListView.as_view(), name='task_list'),
    path('task/create/', TaskCreateView.as_view(), name='task_create'),
    path('task/<int:pk>/edit/', TaskUpdateView.as_view(), name='task_edit'),
    path('task/<int:pk>/delete/', TaskDeleteView.as_view(), name='task_delete'),
    path('task/<int:pk>/details/', TaskDetailView.as_view(), name='task_details'),
    path('tasks/completed/', CompletedTasksListView.as_view(), name='completed_tasks'),
    path('api/task/<int:pk>/toggle_complete/', toggle_task_complete, name='toggle_task_complete'),
    path('comment/<int:pk>/edit/', CommentUpdateView.as_view(), name='comment_edit'),
    path('comment/<int:pk>/delete/', CommentDeleteView.as_view(), name='comment_delete'),
    path('category/', CategoryListView.as_view(), name='category_list'),
    path('category/create/', CategoryCreateView.as_view(), name='category_create'),
    path('category/<int:pk>/edit/', CategoryUpdateView.as_view(), name='category_edit'),
    path('category/<int:pk>/delete/', CategoryDeleteView.as_view(), name='category_delete'),
]
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Task
from .serializers import TaskSerializer

# Api django rest frame
@api_view(['PATCH'])
def toggle_task_complete(request, pk):
    try:
        task = Task.objects.get(pk=pk, user=request.user)
    except Task.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    task.completed = not task.completed
    task.save()
    return Response(TaskSerializer(task).data, status=status.HTTP_200_OK)

from django.shortcuts import render
from .models import Task
from django.shortcuts import render

# Create your views here.
def task_list(request):
    all_task = Task.objects.all()
    return render(request, 'task/list.html', {'all_task': all_task})

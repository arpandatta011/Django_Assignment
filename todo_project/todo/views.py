from django.shortcuts import render, redirect
from .models import Task

# View to display the list of tasks
def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'todo/task_list.html', {'tasks': tasks})

# View to add a new task
def add_task(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        Task.objects.create(title=title)
        return redirect('task_list')  # Redirect to task list view
    return render(request, 'todo/add_task.html')

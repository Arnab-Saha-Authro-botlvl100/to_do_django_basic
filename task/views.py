from django.shortcuts import render, redirect
from .models import Task
from django.contrib import messages
# Create your views here.
from django.shortcuts import render
from .models import Task

def welcome(request):
    tasks = Task.objects.filter(user_id_id=request.user)
    completed_tasks = tasks.filter(completed=True)
    incomplete_tasks = tasks.filter(completed=False)
    print(request.user.id)
    return render(request, 'welcome.html', {
        'title': 'Welcome',
        'tasks': incomplete_tasks,
        'completed_tasks': completed_tasks,
    })

def add_task(request):
    if request.method == 'POST':
        data = request.POST
        title = data.get('task_name')
        description = data.get('task_description')
        due_date = data.get('due_date')
        priority = data.get('priority')
        user_id_id = request.user
        # Validate the input data
        if not all([title, description, due_date, priority, user_id_id]):
            messages.error(request, "All fields are required")
            return render(request, 'welcome.html', {'title': 'Welcome'})


        # Create and save the new task
        Task.objects.create(
            title=title,
            description=description,
            due_date=due_date,
            priority=priority,
            completed=False,
            user_id_id=user_id_id.id,
        )
        messages.success(request, "Task added successfully")
        return redirect('welcome')

    return render(request, 'welcome.html', {'title': 'Welcome'})



def update_tasks(request):
    if request.method == 'POST':
        completed_task_ids = request.POST.getlist('completed_tasks')
        all_tasks = Task.objects.all()
        
        for task in all_tasks:
            task.description = request.POST.get(f'description_{task.id}')
            task.due_date = request.POST.get(f'due_date_{task.id}')
            if str(task.id) in completed_task_ids:
                task.completed = True
            else:
                task.completed = False
            task.save()
        
        messages.success(request, 'Tasks updated successfully.')
        return redirect('welcome')

    return redirect('welcome')
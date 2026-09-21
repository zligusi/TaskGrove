from django.shortcuts import render , redirect
from django.shortcuts import get_object_or_404
from django.http.response import HttpResponseForbidden
from .models import Task
from .forms import TaskForm

def home(request):
    tasks = Task.objects.all()
    return render(request, 'main/home.html', {'tasks': tasks})


def task_detail(request, slug):
    task = Task.objects.get(slug=slug)
    return render(request, 'main/task_detail.html', {'task': task})


def task_create(request):
    if request.method == 'POST':
        form= TaskForm(request.POST, request.FILES)
        if form.is_valid():
            task = form.save(commit=False)
            task.author = request.user
            task.save()
            return redirect('home')
    else:
        form = TaskForm()

    return render(request, 'main/task_create.html', {'form': form})


def task_update(request, slug):
    task = get_object_or_404(Task, slug=slug, author=request.user )
    if request.method == 'POST':
        form = TaskForm(request.POST, request.FILES, instance=task)
        if form.is_valid():
            if request.user != task.author :
                return HttpResponseForbidden ('You do not have permission')
            form.save()
            return redirect('home')
    else:
        form = TaskForm(instance=task)

    return render(request, 'main/task_update.html', {'form': form})

def task_delete(request, slug):
    task = get_object_or_404(Task, slug=slug, author=request.user )
    if request.method == 'POST':
        if request.user != task.author :
                        return HttpResponseForbidden ('You do not have permission')
        task.delete()
        return redirect('home')
    else:
        return render(request, 'main/task_confirm_delete.html', {'task': task})
        




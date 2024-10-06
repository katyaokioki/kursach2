from django.shortcuts import render, redirect, get_object_or_404
from .models import Project, Task, Comment
from .forms import ProjectForm
from .forms import TaskForm, CommentForm
from django.contrib.auth.decorators import login_required

@login_required

def project_list(request):
    projects = Project.objects.all()
    return render(request, 'tasks/project_list.html', {'projects': projects})

def add_project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('project_list')
    else:
        form = ProjectForm()
    return render(request, 'tasks/add_project.html', {'form': form})

def edit_project(request, pk):
    project = get_object_or_404(Project, pk=pk)
    if request.method == 'POST':
        form = ProjectForm(request.POST, instance=project)
        if form.is_valid():
            form.save()
            return redirect('project_list')
    else:
        form = ProjectForm(instance=project)
    return render(request, 'tasks/edit_project.html', {'form': form})

def delete_project(request, pk):
    project = get_object_or_404(Project, pk=pk)
    if request.method == 'POST':    
        project.delete()
        return redirect('project_list')
    return render(request, 'tasks/delete_project.html', {'project': project})


def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk)
    tasks = project.tasks.all()

    if request.method == 'POST':
        if 'add_task' in request.POST:
            form = TaskForm(request.POST)
            if form.is_valid():
                task = form.save(commit=False)
                task.project = project
                task.save()
                return redirect('project_detail', pk=project.pk)
        elif 'edit_task' in request.POST:
            task_id = request.POST.get('task_id')
            task = get_object_or_404(Task, id=task_id)
            form = TaskForm(request.POST, instance=task)
            if form.is_valid():
                form.save()
                return redirect('project_detail', pk=project.pk)
        elif 'delete_task' in request.POST:
            task_id = request.POST.get('task_id')
            task = get_object_or_404(Task, id=task_id)
            task.delete()
            return redirect('project_detail', pk=project.pk)

    else:
        form = TaskForm()

    return render(request, 'tasks/project_detail.html', {'project': project, 'tasks': tasks, 'form': form})

def task_comments(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    comments = task.comments.all()

    if request.method == 'POST':
        if 'add_comment' in request.POST:
            form = CommentForm(request.POST)
            if form.is_valid():
                comment = form.save(commit=False)
                comment.task = task
                comment.user = request.user
                comment.save()
                return redirect('task_comments', task_id=task.id)

        elif 'edit_comment' in request.POST:
            comment_id = request.POST.get('comment_id')
            comment = get_object_or_404(Comment, id=comment_id)
            form = CommentForm(request.POST, instance=comment)
            if form.is_valid():
                form.save()
                return redirect('task_comments', task_id=task.id)

        elif 'delete_comment' in request.POST:
            comment_id = request.POST.get('comment_id')
            comment = get_object_or_404(Comment, id=comment_id)
            comment.delete()
            return redirect('task_comments', task_id=task.id)

    else:
        form = CommentForm()

    return render(request, 'tasks/task_comments.html', {
        'task': task,
        'comments': comments,
        'form': form,
    })


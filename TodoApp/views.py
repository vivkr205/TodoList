from django.shortcuts import render,redirect
from django.http import HttpResponse
from TodoApp.models import Tasklist
from TodoApp.forms import TaskForm
from django.contrib import messages
from django.utils import timezone
from django.contrib.auth.decorators import login_required



# Create your views here.
def home(request):
    return render(request,'home.html')

@login_required
def todolist(request):
    if request.method=="POST":
        form=TaskForm(request.POST or None)
        if form.is_valid():
            instance=form.save(commit=False)
            instance.manage_id=request.user
            instance.save()
        messages.success(request,('Task Added✅'))
        return redirect('todolist')
    else:
        all_tasks=Tasklist.objects.filter(manage_id=request.user)
        return render(request,'todolist.html',{'all_tasks':all_tasks})
    
def delete(request, task_id):
        task = Tasklist.objects.get(pk=task_id)
        if task.manage_id == request.user: 
           task.delete()
           messages.success(request, 'Task deleted successfully!')
        else:
            messages.error(request, 'Not Allowed!')
        return redirect('todolist')
   
@login_required 
def mark_done(request, task_id):
    task = Tasklist.objects.get(pk=task_id)
    if task.manage_id == request.user:
        task.done = True
        task.save()
    else:
        messages.error(request, 'Not Allowed!')
    return redirect('todolist')
 
@login_required
def mark_pending(request, task_id):
    task = Tasklist.objects.get(pk=task_id)
    if task.manage_id == request.user:
        task.done = False
        task.save()
    else:
        messages.error(request, 'Not Allowed!')
    return redirect('todolist')
        
               
def edit_task(request, task_id):
    if request.method=="POST":
        task = Tasklist.objects.get(pk=task_id)
        form=TaskForm(request.POST or None, instance=task)
        if form.is_valid():
            form.save()
            task.date_modified = timezone.now()
            task.save()
        messages.success(request, 'Task edited successfully!')
        return  redirect('todolist')    
    else:
        task_obj=Tasklist.objects.get(pk=task_id)
        return render(request,'edit_task.html',{'task_obj':task_obj})

@login_required
def contact(request):
    return render(request,'contact.html')

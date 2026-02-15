from django.shortcuts import redirect, render
from .models import Category, Task 
from django.contrib.auth.decorators import login_required
from .forms import TaskForm


@login_required
def dashboard(request):
     Category.objects.get_or_create(user=request.user, name="General")
     tasks = Task.objects.filter(user=request.user)
     return render(request, "tasks/dashboard.html", {"tasks": tasks})

@login_required
def create_task(request): 
     Category.objects.get_or_create(user=request.user, name="General")
     if request.method == "POST":
          form = TaskForm(request.POST, user=request.user) 
          if form.is_valid(): 
               task = form.save(commit=False) 
               task.user = request.user 
               task.save() 
               return redirect("dashboard")
     else:
          form = TaskForm(user=request.user)
     return render(request, "tasks/create_task.html", {"form": form})


@login_required
def delete_task(request, task_id):
     if request.method == "POST":
          Task.objects.filter(id=task_id, user=request.user).delete()
     return redirect("dashboard")

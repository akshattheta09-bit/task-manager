from django.shortcuts import redirect, render
from .models import Task 
from django.contrib.auth.decorators import login_required
from .forms import TaskForm


@login_required
def dashboard(request):
     tasks = Task.objects.filter(user=request.user)
     return render(request, "tasks/dashboard.html", {"tasks": tasks})

@login_required
def create_task(request): 
     if request.method == "POST":
          form = TaskForm(request.POST) 
          if form.is_valid(): 
               task = form.save(commit=False) 
               task.user = request.user 
               task.save() 
               return redirect("dashboard")
     else:
          form = TaskForm()
     return render(request, "tasks/create_task.html", {"form": form})

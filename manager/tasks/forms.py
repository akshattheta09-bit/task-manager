from django import forms 
from .models import Category, Task

class TaskForm(forms.ModelForm):
    def __init__(self, *args, user=None, **kwargs):
        super().__init__(*args, **kwargs)
        if user is not None:
            self.fields["category"].queryset = Category.objects.filter(user=user).order_by("name")

    class Meta:
        model = Task
        fields = ["title", "description", "due_date", "status", "category"]
        widgets = {
            "due_date": forms.DateInput(attrs={"type": "date"}),
        }
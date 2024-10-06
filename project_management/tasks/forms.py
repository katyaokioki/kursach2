from django import forms
from .models import Project
from .models import Task
from .models import Comment

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['name', 'description', 'start_date', 'end_date']

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'due_date']  # Укажите поля, которые хотите использовать в форме
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
from django.db import models
from django.contrib.auth.models import User

class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    users = models.ManyToManyField(User, related_name='projects')

class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    due_date = models.DateField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='tasks')
    tags = models.ManyToManyField('Tag', related_name='tasks', blank=True)  # Используем строковое представление

class Tag(models.Model):
    name = models.CharField(max_length=30)
    # Здесь определение поля ManyToMany не требуется, так как оно уже определено в Task

class User(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField(blank=True, null=True)

class Assignment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)

class Comment(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    text = models.TextField(default='')


 

# from django.db import models
# from django.contrib.auth.models import User  # Используем встроенную модель User

# class Project(models.Model):
#     name = models.CharField(max_length=100)
#     description = models.TextField()
#     start_date = models.DateField()
#     end_date = models.DateField()
#     users = models.ManyToManyField(User, related_name='projects')  # Поле Many-to-Many

# class Task(models.Model):
#     title = models.CharField(max_length=100)
#     description = models.TextField()
#     due_date = models.DateField()
#     project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='tasks')

# class Assignment(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     task = models.ForeignKey(Task, on_delete=models.CASCADE)

# class Comment(models.Model):
#     task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='comments')
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     content = models.TextField()  # Оставляем только это поле
#     created_at = models.DateTimeField(auto_now_add=True)

# class Tag(models.Model):
#     name = models.CharField(max_length=30)
#     tasks = models.ManyToManyField(Task, related_name='tags')
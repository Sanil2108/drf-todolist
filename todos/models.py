from django.db import models

from users.models import User

class TodoList(models.Model):
    # Check on_delete
    owner = models.ForeignKey(User, on_delete = models.CASCADE)
    title = models.CharField(max_length = 100)
    private = models.BooleanField(default = False)

class TodoItem(models.Model):
    # Check on_delete
    todoList = models.ForeignKey(TodoList, on_delete = models.CASCADE)
    done = models.BooleanField(default = False)
    name = models.CharField(max_length = 100)
    description = models.CharField(max_length = 1000)

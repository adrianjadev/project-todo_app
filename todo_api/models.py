from django.db import models

# Create your models here.


class Todo(models.Model):
    title = models.CharField(max_length=250)
    description = models.CharField(max_length=250)
    date_created = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now_add=True)
    isCompleted = models.BooleanField(default=False)

    def __str__(self):
        return f'Task: {self.title}'

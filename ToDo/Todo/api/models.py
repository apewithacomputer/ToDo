from django.db import models


class Todo(models.Model):
    tasks = models.TextField(max_length=125)
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now_add=True)

    def __self__(self):
        return self.tasks

    class Meta:
        ordering = ['-created']

from django.db import models


class Accounts(models.Model):
    username = models.TextField(max_length=125)
    password = models.TextField(max_length=125)

    def __self__(self):
        return self.tasks

from django.db import models


# Create your models here.
class List(models.Model):
    title = models.CharField(max_length=250, unique=True)

    def __str__(self):
        return self.title


class Item(models.Model):
    title = models.CharField(max_length=250)

    completed = models.BooleanField(default=False)

    todo_list = models.ForeignKey(List)

    def __str__(self):
        return self.title

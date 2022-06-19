from django.db import models
from django.contrib.auth import get_user_model
user_model = get_user_model()

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200, blank = True)
    text = models.TextField()
    author = models.ForeignKey(user_model, on_delete=models.CASCADE)
    created_date = models.DateTimeField()
    published_date= models.DateTimeField()

    def __str__(self):
        return f'{self.title}'


"""
defines a table name, the columns that'll appear on the table, and the datatypes(/conditions) that'll be used in this column
like CREATE_TABLE command in SQL.

2 specific commands that work here: python manage.py makemigrations(uses instructions in model file and create a sql statement) and python mange.py migrate (uses the sql statement in the previous step and applies it to a database)
"""

#f"{self.title} {self.new_field}"
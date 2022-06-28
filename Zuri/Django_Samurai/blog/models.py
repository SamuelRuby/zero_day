from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone
from django.urls import reverse
from django.template.defaultfilters import slugify

user_model = get_user_model()

# Create your models here.
class Post(models.Model):

    STATUS_CHOICES = (
        ("draft", "Draft"),
        ("published", "Published")
    )

    # DB Fields
    title = models.CharField(max_length=250, blank = True)
    slug = models.SlugField(max_length=300, unique=True, editable=False, null = True)
    text = models.TextField()
    author = models.ForeignKey(user_model, on_delete=models.CASCADE, related_name="blog_posts")
    created_date = models.DateTimeField(auto_now_add=True)
    published_date= models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(auto_now=True)

    status = models.CharField(
        max_length=10, choices=STATUS_CHOICES, default="draft"
    )

    class Meta:
        ordering = ("-published_date",)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)
        pass 

    def get_absolute_url(self):
        absolute_url = reverse("blog:post_detail", kwargs={"slug": self.slug})
        print (absolute_url)
        return absolute_url

    def __str__(self):
        return f'{self.title}'


"""
defines a table name, the columns that'll appear on the table, and the datatypes(/conditions) that'll be used in this column
like CREATE_TABLE command in SQL.

2 specific commands that work here: python manage.py makemigrations(uses instructions in model file and create a sql statement) and python mange.py migrate (uses the sql statement in the previous step and applies it to a database)
"""

#f"{self.title} {self.new_field}"
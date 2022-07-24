from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone
from django.urls import reverse
from django.template.defaultfilters import slugify
from .managers import ActiveLinkManager

user_model = get_user_model()
class Link(models.Model):
    

# Create your models here.
    target_url = models.URLField(max_length=200)
    description = models.CharField(max_length=200, blank = True)
    identifier = models.SlugField(max_length=300, blank = True, unique=True, null = True)
    author = models.ForeignKey(user_model, on_delete=models.CASCADE, related_name="links")
    created_date = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField()
    objects = models.Manager()
    
    public = ActiveLinkManager()
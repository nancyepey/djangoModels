from django.db import models

from django.contrib.auth import get_user_model

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    author = models.ForeignKey(
        get_user_model(),
        null=True, # explicitly set null, since it's required in django 2.x. - otherwise migrations will be incompatible later!
        on_delete=models.CASCADE,
    )
    created_date = models.DateTimeField()
    published_date = models.DateTimeField()

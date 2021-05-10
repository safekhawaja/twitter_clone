from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Hashtag(models.Model):

    name = models.CharField(max_length = 20)


class Tweet(models.Model):
    # text, author, date

    text = models.CharField(max_length = 180)
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    time = models.DateTimeField(auto_now=True)
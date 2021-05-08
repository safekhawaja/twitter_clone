from django.db import models

# Create your models here.

class User(models.Model):

    name = models.CharField(max_length = 20)
    secret = models.CharField(max_length = 20)
    email = models.CharField(max_length = 40)


class Tweet(models.Model):
    # text, author, hashtags, date

    text = models.CharField(max_length = 180)
    # author = user
    time = models.DateTimeField(auto_now_add=True)
from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=400)
    body = models.TextField()

class DummyPost(models.Model):
    title = models.CharField(max_length=400)
    body = models.TextField()

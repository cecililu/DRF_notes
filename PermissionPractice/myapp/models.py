from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=400)
    body = models.TextField()

class DummyPost(models.Model):
    title = models.CharField(max_length=400)
    body = models.TextField()


class PostModelLEvel(models.Model):
    title = models.CharField(max_length=400)
    body = models.TextField()
    is_published = models.BooleanField(default=False)


    class Meta:
        permissions = [
            (
                "set_published_status",
                "Can set the status of the post to either publish or not"
            )    ]
        
class MuniModel(models.Model):
    name=name=models.CharField(max_length=100)
       
class DisasterModel(models.Model):
    name=models.CharField(max_length=100)
    muni=models.ForeignKey(MuniModel,on_delete=models.CASCADE)
    
    
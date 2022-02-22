from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Comments(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    video_id = models.CharField(max_length=30)
    text = models.CharField(max_length=500)
    likes = models.IntegerField()
    dislikes = models.IntegerField()

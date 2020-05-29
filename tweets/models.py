from django.db import models

# Create your models here.
class Tweet(models.Model):
    content=models.TextField(blank=True,null=True)
    image=models.ImageField( upload_to='media/images',blank=True,null=True)
    
from django.db import models
from datetime import datetime

class ShowManager(models.Manager):
    def validate(self, postInfo):
        print(postInfo['release_date'])
        errors = {}
        if len(postInfo['title']) < 2:
            errors['title'] = 'Title field is less than 2 characters'
        if len(postInfo['network']) < 3:
            errors['network'] = 'Network field is less than 3 characters'
        if len(postInfo['desc']) < 10 and postInfo['desc'] != 0:
            errors['desc'] = 'Description is less than 10 characters'
        #if postInfo['release_date'] != 0:
        if datetime.strptime(postInfo['release_date'], '%Y-%m-%d') > datetime.now():
            errors['release_date'] = 'Release Date should be in the past'
        return errors

# Create your models here.
class Show(models.Model):
    title = models.CharField(max_length=150)
    network = models.CharField(max_length=150)
    release_date = models.DateTimeField(auto_now_add=True)
    desc = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    objects = ShowManager()

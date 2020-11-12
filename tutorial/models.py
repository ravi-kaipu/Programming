from django.db import models
from datetime import date
from django.core.validators import RegexValidator
import uuid
from django.conf import settings

import os


class AddMainTopic(models.Model):
    language =  models.CharField(max_length=10000)
    topicname = models.CharField(max_length=10000)
    topictype = models.CharField(max_length=10000)
    description = models.TextField(max_length=10000)
    syntax = models.TextField(max_length=10000)
    example = models.TextField(max_length=10000)
    output = models.TextField(max_length=10000, default="")

    @property
    def subtopics(self):
        return self.addsubtopic_set.all()
    
    @property
    def strip(value):
        print("dkfd", value)
        return value.strip()

    def __str__(self):
        return self.topicname
    

class AddSubTopic(models.Model):
    maintopic = models.ForeignKey(AddMainTopic, default=None, on_delete=models.CASCADE)
    topicname = models.CharField(max_length=10000)
    topictype = models.CharField(max_length=10000)
    description = models.TextField(max_length=10000)
    syntax = models.TextField(max_length=10000)
    example = models.TextField(max_length=10000)
    output = models.TextField(max_length=10000)

    def __str__(self):
        return self.topicname

class Image(models.Model):
    owner = models.ForeignKey(AddMainTopic, default=None, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=os.path.join(settings.STATIC_ROOT, "tutorial/private_images/"))

    def filename(self):
        return str(os.path.basename(self.image.url))

    def __str__(self):
        return self.owner.foodname


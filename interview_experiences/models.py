from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField


# Create your models here.



class experience(models.Model):
    title = models.TextField(unique=True,default='')
    company = models.CharField(max_length=200)
    type_offer = models.CharField(max_length=200)
    job_profile = models.CharField(max_length=200)
    username = models.ForeignKey(User,on_delete=models.CASCADE,default=1)
    author = models.CharField(max_length=200)
    year = models.IntegerField()
    timestamp = models.DateTimeField(auto_now=True)
    content = RichTextField(blank=True,null=True)
    slug = models.CharField(max_length=200)
    bookmark = models.ManyToManyField(User,related_name='bookmark',default=None)


    def __str__(self):
        return self.company + self.author


class comment(models.Model):
    content = models.TextField(max_length=500)
    writer = models.ForeignKey(User,on_delete=models.CASCADE,default=1)
    exp = models.ForeignKey(experience,on_delete=models.CASCADE)
    parent = models.ForeignKey('self',on_delete=models.CASCADE,null=True)
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.content[0:15] + "by " + self.writer.first_name
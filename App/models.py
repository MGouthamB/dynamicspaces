from django.db import models
import time
from ckeditor.fields import RichTextField
from django.utils import timezone
from datetime import datetime
# Create your models here.
class Jobs(models.Model):
    title= models.CharField(max_length=500)
    keywords=models.CharField(max_length=500)
    company=models.CharField(max_length=500,default="")
    sdescription=models.CharField(max_length=500)
    description=RichTextField()
    background_img_url = models.CharField(max_length=500)
    logo_img_url = models.CharField(max_length=500)
    location=models.CharField(max_length=500)
    eemail = models.CharField(max_length=500)
    expire_in_days=models.DateField(null=True)
    time=models.DateField(editable=False,default=timezone.now)
    posted_by=models.CharField(max_length=500)
    need_files = models.BooleanField(default=False)

class Profiles(models.Model):
    name = models.CharField(max_length=500)
    email = models.CharField(max_length=500,unique=True)
    username = models.CharField(max_length=500)
    password = models.CharField(max_length=500)
    company = models.CharField(max_length=500)
    job = models.CharField(max_length=500)
    account_type = models.CharField(max_length=500, default="Job")
    email_verfied = models.BooleanField(default=False)
    subscriber = models.BooleanField(default=False)
    subscriber_id = models.CharField(max_length=500,default="")
    key = models.CharField(max_length=500)
    img_url = models.CharField(max_length=500,default="https://static.vecteezy.com/system/resources/previews/005/544/718/original/profile-icon-design-free-vector.jpg")
    # profile_pic = models.ImageField(upload_to='images')

class JobApplication(models.Model):
    job = models.ForeignKey("Jobs", on_delete=models.CASCADE)
    name = models.CharField(max_length=100,blank=False)
    email = models.EmailField(blank=False)
    address = models.TextField()
    resume_link = models.URLField()

class FormData(models.Model):
    data = models.CharField(max_length=2000)
    posted_for = models.CharField(max_length=500)
    time = models.DateField(editable=False, default=timezone.now)
    form_name = models.CharField(max_length=500)

class Content(models.Model):
    title = models.CharField(max_length=500)
    subtitle = models.CharField(max_length=2000)
    description = models.TextField()
    posted_by=models.CharField(max_length=500)
    key = models.CharField(max_length=500)
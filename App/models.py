from django.db import models
import time
from ckeditor.fields import RichTextField
from django.utils import timezone
from datetime import datetime
# Create your models here.
class Jobs(models.Model):
    title= models.CharField(max_length=500)
    keywords=models.CharField(max_length=500,blank=True)
    company=models.CharField(max_length=500,default="")
    sdescription=models.CharField(max_length=500)
    description=RichTextField(blank=True)
    background_img_url = models.CharField(max_length=500,blank=True)
    logo_img_url = models.CharField(max_length=500,blank=True)
    location=models.CharField(max_length=500)
    eemail = models.CharField(max_length=500)
    expire_in_days=models.DateField(null=True)
    time=models.DateField(editable=True,default=timezone.now)
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

class IntegrationJobApplication(models.Model):
    title = models.CharField(max_length=100,blank=False)
    eemail = models.CharField(max_length=100)
    name = models.CharField(max_length=100,blank=False)
    email = models.EmailField(blank=False)
    posted_by = models.EmailField(blank=False)
    resume_link = models.URLField()

class FormData(models.Model):
    data = models.TextField(default="")
    posted_for = models.CharField(max_length=500)
    time = models.DateField(editable=False, default=timezone.now)
    form_name = models.CharField(max_length=500)

class Content(models.Model):
    title = models.CharField(max_length=500)
    subtitle = models.CharField(max_length=2000)
    description = models.TextField()
    posted_by=models.CharField(max_length=500)
    key = models.CharField(max_length=500)

class Integration(models.Model):
    name = models.CharField(max_length=500)
    logo = models.CharField(max_length=500)
    links = models.TextField()

class AccountIntegrations(models.Model):
    integration = models.ForeignKey("Integration", on_delete=models.CASCADE)
    account = models.CharField(max_length=500)
    email = models.CharField(max_length=500)
    password = models.CharField(max_length=500)
    api_key = models.CharField(max_length=500)
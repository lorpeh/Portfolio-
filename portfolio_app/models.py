from django.db import models
from datetime import datetime, time

# Create your models here.
#HOME SECTION
class Home(models.Model):
    name= models.CharField(max_length=30)
    greetings_1 = models.CharField(max_length=30 )
    greetings_2 = models.CharField(max_length=30)
    pictures = models.ImageField(upload_to ='picture/')
    updated = models.DateTimeField(auto_now=True)
     
     
    def __str__(self):
        return self.name
    # first_name = models.CharField(max_length=40)
    # last_name = models.CharField(max_length=40)

#ABOUT SECTION

class About(models.Model):
    heading = models.CharField(max_length=300)
    career = models.CharField(max_length=30)
    description = models.TextField(blank=False)
    profile_img = models.ImageField(upload_to='profile/')
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.career

class Profile(models.Model):
    about = models.ForeignKey(About, on_delete=models.CASCADE)
    social_name = models.CharField(max_length=10)
    link = models.URLField(max_length=200)


#SKILL SECTION
class Category(models.Model):
    name = models.CharField(max_length=50)
    updated = models.DateTimeField(auto_now_add=True)

    class meta:
        verbose_name = 'skill'
        verbose_name_plural = 'skills'

    def __str__(self):
        return self.name

class Skill(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)   

    skill_name = models.CharField(max_length=30)

#PORTFOLIO SECTION

class Portfolio(models.Model):
    image = models.ImageField(upload_to='portfolio/')
    link = models.URLField(max_length=300)

    def __str__(self): 
        return f"Portfolio {self.id}"   

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Project(models.Model):
   name = models.CharField(null=True, max_length=100)
   description = models.TextField(null=True)
   users = models.ManyToManyField(User)
   
   def __str__(self):
       return self.name
    
   def save(self, *args, **kwargs):
        # Check if the project is being created (not already in the database)
        if not self.pk:
            # Assuming you are using Django's authentication system
            # Get the currently logged-in user
            user = kwargs.pop('user', None)
            if user:
                # Add the user to the project's users field
                self.users.add(user)

        super().save(*args, **kwargs)


class Survey(models.Model):
   
     locale={
        ('beach','beach'),
        ('city','city'),
        ('remote','remote'),
        
     }
     stay ={
        ('hotel','hotel'),
        ('airbnb','airbnb'),
        ('motel','motel'),
        
     }
   
   
     project = models.ForeignKey(Project,null=True,on_delete =models.SET_NULL,)
     name = models.CharField(null=True, max_length=100)
     location = models.CharField(max_length=100,null=True, choices=locale)
     accomodation = models.CharField(max_length=100, null=True, choices=stay)
     guests = models.IntegerField(null=True)
     rating = models.IntegerField(null= True)
     leisure = models.CharField(max_length=100,null=True)
     checkin = models.DateField(null=True)
     checkout = models.DateField(null=True)
     
     
     def __str__(self):
        return self.location

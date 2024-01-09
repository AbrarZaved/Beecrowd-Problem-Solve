from django.db import models
from users.models import Profile
import uuid
class info(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    demo_link = models.CharField(max_length=2000, blank=True, null=True)
    source_link = models.CharField(max_length=2000, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, 
                          primary_key=True, editable=False)
    
    def __str__(self):
        return self.title


class CLUB(models.Model):
    owner = models.ForeignKey(Profile,null=True,blank=True,on_delete=models.SET_NULL)
    name =  models.CharField(max_length=100,blank=False,null=False)
    Student_ID= models.CharField(max_length=20,blank=False,null=False)
    Student_Mail = models.CharField(max_length=50,blank=False,null=False)
    Image=models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=None,default="static/user.png")
    Phone_Number =  models.CharField(max_length=20,blank=False,null=False)
    Preferred_Club = models.CharField(max_length=100,blank=False,null=False)
    tags = models.ManyToManyField('Tag',blank=True)
    votes_total = models.IntegerField(default=0, null=True, blank=True)
    vote_ratio = models.IntegerField(default=0, null=True, blank=True)
    Reason_behind_joinning_club = models.TextField(max_length=2000,blank=False,null=False)
    created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name
    
class Review(models.Model):
    VOTE_TYPE = (
        ('up','Up Vote'),
        ('down','Down Vote')
    )
    #owner =
    
    project = models.ForeignKey(CLUB, on_delete=models.CASCADE) 
    body = models.TextField(null=True, blank=True)
    value = models.CharField(max_length=200, choices=VOTE_TYPE)
    created = models.DateTimeField(auto_now_add=True)
    id  = models.UUIDField(default=uuid.uuid4, unique=True, 
                                primary_key=True, editable=False)
    
    def __str__(self):
        return self.value

class Tag(models.Model):
    name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    id  = models.UUIDField(default=uuid.uuid4, unique=True, 
                                primary_key=True, editable=False)
    
    def __str__(self):
        return self.name
        
    

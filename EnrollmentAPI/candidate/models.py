from django.db import models
from enrollment.models import Enrollment
#from uuid import uuid4

class Candidate(models.Model):
    #id = models.UUIDField(primary_key=True,default=uuid4,editable=False)
    name = models.CharField(max_length=120, default='')    
    email = models.EmailField(default='', unique=True)
    password = models.CharField(max_length=10, default='')
    profile = models.IntegerField(default=2)
    enrollment = models.ManyToManyField(Enrollment, blank=True) 
    time_online = models.BigIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
   
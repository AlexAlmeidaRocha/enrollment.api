from django.db import models
#from uuid import uuid4

class Enrollment(models.Model):
    #id = models.UUIDField(primary_key=True,default=uuid4,editable=False)
    name = models.CharField(max_length=120, unique=True)    
    created_at = models.DateTimeField(auto_now_add=True)

from django.db import models
from datetime import datetime
time = datetime.now()
# Create your models here.
class Notes(models.Model):
    title = models.CharField(max_length=20) # 255
    description = models.TextField()
    datetime = models.DateTimeField(auto_now=time)
    

from django.db import models


# Create your models here.

class employees(models.Model): 
    id=models.AutoField(primary_key=True)  
    Email = models.CharField(max_length=100)
    FirstName = models.CharField(max_length=100)
    LastName = models.CharField(max_length=100)
    
    class Meta:
        db_table = "employees"


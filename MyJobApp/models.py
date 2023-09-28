from django.db import models

# Create your models here.
class Student(models.Model):
    email=models.EmailField()
    password=models.CharField(max_length=100)
    comformpassword=models.CharField(max_length=100)
    
from django.db import models

class JobTable(models.Model):
    jobname = models.CharField(max_length=100)
    image = models.ImageField(upload_to='job_images/')
    postdescription = models.TextField()
    people_required = models.IntegerField()
    job_type = models.CharField(max_length=50)
    salary = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.jobname

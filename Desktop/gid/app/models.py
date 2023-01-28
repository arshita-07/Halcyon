from django.db import models
from users.models import *
from django.utils import timezone
from django.urls import reverse
from datetime import date
 
# Create your models here.
#Resource-->Resource
#recruiter-->hospital
#Recruiter-->Hospital
#resource_description-->resource_decription
#apply_deadline-->available deadline
#required_skills --> quantity
#work_from_home --> price
#cv-->medical_history
class Resource(models.Model):
    title = models.CharField(max_length = 300, null = False )
    hospital = models.ForeignKey(Hospital,on_delete=models.CASCADE, related_name="hospital")
    resource_description = models.TextField(null = False)
    date_posted = models.DateTimeField(default = timezone.now)
    keywords = models.CharField(max_length = 200,null=False, default='NA')
    applicants = models.ManyToManyField(ClientUser,through='Application',related_name = "applicants")
    status = models.BooleanField(default=False)
    quantity = models.IntegerField(null=False)
    available_deadline = models.DateField(verbose_name='Available till',null=True)
    location = models.CharField(max_length=300, null=False)
    price = models.CharField(max_length = 200, null = False, default="0")

    def get_absolute_url(self):
        return reverse('detail', kwargs={'pk':self.pk})

    @property
    def is_past_due(self):
        return date.today() > self.apply_deadline
 

class Application(models.Model):
    applicant = models.ForeignKey(ClientUser,on_delete=models.CASCADE, related_name="applicant")
    resource = models.ForeignKey(Resource, on_delete=models.CASCADE, related_name='resource')
    medical_history = models.FileField(upload_to='medical_history')
    
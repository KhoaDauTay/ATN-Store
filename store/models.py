from django.db import models

# Create your models here.
class Patient(models.Model):
    ptName = models.CharField(max_length=100, blank=False, null=False)
    ptIdCard = models.IntegerField()
    ptPrice = models.FloatField()
    ptPhone = models.CharField(max_length=100, blank=False, null=False)
    Name = models.CharField(max_length=100, blank=False, null=False)
    def __str__(self):
        return self.ptName
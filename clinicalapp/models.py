from django.db import models

class Patient(models.Model):
    lastname = models.CharField(max_length=200)
    firstname = models.CharField(max_length=200)
    age = models.IntegerField()

class ClinicalData(models.Model):
    COMPONENT_NAMES = [('hw','Height/Weight'),('bp','Blood Pressure'),('heartrate','Heart Rate')]
    componentName = models.CharField(choices = COMPONENT_NAMES,max_length=200)
    componentvalue = models.CharField(max_length=200)
    measuredDateTime = models.DateTimeField(auto_now_add=True)
    patient = models.ForeignKey(Patient,on_delete=models.CASCADE)



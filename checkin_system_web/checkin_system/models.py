from django.db import models


# Create your models here.
class Hrdata(models.Model):
    employee_id = models.CharField(max_length=11, primary_key=True)
    english_name = models.CharField(max_length=50)
    department_id = models.CharField(max_length=10)
    supervisor_id = models.CharField(max_length=11)

    class Meta:
        ordering = ['employee_id']


class Checkindata(models.Model):
    employee_id = models.CharField(max_length=11)
    checkin_date = models.DateField(auto_now_add=True)
    timein = models.DateTimeField(null=True)
    timeout = models.DateTimeField(null=True)

    class Meta:
        unique_together = [
            'employee_id', 'checkin_date'
        ]
        ordering = ['employee_id', ]

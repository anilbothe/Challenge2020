from django.db import models

# Audit data
class WeatherAudit(models.Model):
    city        = models.CharField(max_length=10, null=True)
    temperature = models.CharField(max_length=10, null=True)
    description = models.CharField(max_length=10, null=True)
    icon        = models.ImageField(upload_to='icons', null=True)
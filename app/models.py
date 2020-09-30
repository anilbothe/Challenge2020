from django.db import models

class WeatherAudit(models.Model):
    """ Audit data """
    city        = models.CharField(max_length=10, null=True)
    temperature = models.CharField(max_length=10, null=True)
    description = models.CharField(max_length=10, null=True)
    icon        = models.ImageField(upload_to='icons', null=True)

    def __str__(self):
        return self.city
        
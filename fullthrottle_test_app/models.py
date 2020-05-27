from django.db import models


# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=70)
    id = models.CharField(max_length=10, primary_key=True)
    timezone = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.id}'


class ActivityPeriod(models.Model):
    u_id = models.CharField(max_length=10, null=True)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    def __str__(self):
        return f'{self.u_id}'

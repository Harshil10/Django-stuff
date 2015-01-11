from django.db import models

class TELEMETRY_NEW10(models.Model):
    iden = models.IntegerField()
    month = models.IntegerField()
    total_manualscan = models.TextField()
    total_detected_apps = models.TextField()

class TelemetryHrm(models.Model):
    month = models.IntegerField()
    total_manualscan = models.IntegerField()
    total_detected_apps = models.IntegerField()
    total_outdated_apps = models.IntegerField()
    total_vulnerable_apps = models.IntegerField()
    
class Harshil10(models.Model):
    month = models.IntegerField()
    counter_name = models.TextField()
    counter_value = models.IntegerField()
    machine_count = models.IntegerField()
    total_count = models.IntegerField()

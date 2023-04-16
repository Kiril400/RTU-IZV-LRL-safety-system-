from django.db import models

class LabUser(models.Model):
    card_id = models.CharField(max_length=8)
    username = models.CharField(max_length=64)
    year_grad = models.IntegerField()
    access_to_lab = models.BooleanField(default=False)
    last_modified = models.DateTimeField(auto_now=True)
    date_added = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.card_id

class Event(models.Model):
    time = models.DateTimeField(auto_now_add=True)
    card_id = models.CharField(max_length=8)
    event_type = models.CharField(max_length=100)
    def __str__(self):
        return self.card_id + ' ' + self.event_type

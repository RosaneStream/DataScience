from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Event(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    initial_date = models.DateTimeField()
    creation_date = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = "event"

    def __str__(self):
        return self.title
    def get_initial_date(self):
        return self.initial_date.strftime('%d/%m/%Y %H:%M Hrs')

    def get_input_initial_date(self):
        return self.initial_date.strftime('%Y-%m-%dT%H:%M')

    def get_late_event(self):
        if self.initial_date < datetime.now():
            return True
        else:
            return False
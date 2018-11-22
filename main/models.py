from django.db import models
from django.utils import timezone


class Trial(models.Model):
    text = models.TextField()
    published_date = models.DateTimeField(blank=True, null=True)
    created_date = models.DateTimeField(default=timezone.now)
    title = models.CharField(max_length=300)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


"""class Guest(models.Model):
    first_name = models.TextField(default="Osoba")
    second_name = models.TextField(default="Towarzysząca")
    attending = models.BooleanField(default=False)
    modified = models.BooleanField(default=False)
    transport_needed = models.BooleanField(default=False)
    night_needed = models.BooleanField(default=False)
    child = models.BooleanField(default=False)
    comments = models.TextField(max_length=500, default="")

    def publish(self, name, surname, child=False):
        self.first_name = name
        self.second_name = surname
        self.child = child

    def set_attendance(self, attendance):
        self.attending = attendance
        self.modified = True

    def set_transport(self, transport):
        self.transport_needed = transport
        self.modified = True

    def set_night(self, night):
        self.night_needed = night
        self.modified = True

    def send_comments(self, comments):
        self.comments = comments
"""

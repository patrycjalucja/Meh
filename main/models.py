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


class GuestManager(models.Manager):
    def create_guest(self, name, surname, comments, bus, overnight):
        guest = self.create(name=name, surname=surname, comments=comments, bus=bus, overnight=overnight)
        return guest


class Guest(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=50)
    bus = models.BooleanField()
    overnight = models.BooleanField()
    comments = models.CharField(max_length=1000)

    objects = GuestManager()

    def add(self, name, surname, comments, bus=False, overnight=False):
        self.name = name
        self.surname = surname
        self.comments = comments
        self.bus = bus
        self.overnight = overnight

    def __str__(self):
        return self.name + " " + self.surname

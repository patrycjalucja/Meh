from django.db import models
from django.utils import timezone


class Trial(models.Model):
    text = models.TextField()
    published_date = models.DateTimeField(blank=True, null=True)
    created_date = models.DateTimeField(default=timezone.now)
    title = models.CharField(max_length= 300)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

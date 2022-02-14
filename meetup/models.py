from django.db import models
from django.urls import reverse

# Create your models here.

class Location(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=300)

    def __str__(self):
        return self.name

class Participant(models.Model):
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.email


class MeetUp(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    organizer_email = models.EmailField()
    description = models.TextField()
    image = models.ImageField(upload_to="images")
    date = models.DateTimeField(auto_now=True)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    participants = models.ManyToManyField(Participant, blank=True, null=True)

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('meetup:meet_detail', kwargs={'slug':self.slug})

from django.db import models

# Create your models here.
from django.db import models
from django.utils import timezone
from django.urls import reverse
from users.models import User

class Event(models.Model):
    auther =models.ForeignKey("users.Manager", on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    date = models.DateTimeField()
    attendees = models.ManyToManyField(User,blank=True)
    discription = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True,null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()
    
    def add_attendee(self,user):
        self.attendees.add(user)
        self.save()

    def remove_attendee(self,user):
        self.attendees.remove(user)
        self.save()

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("event_detail", kwargs={"pk": self.pk})
 
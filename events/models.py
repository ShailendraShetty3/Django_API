from django.db import models


class Venue(models.Model):
    name = models.CharField('Venue Name', max_length=200)
    address = models.CharField(max_length=300)
    zip_code = models.CharField(max_length=100)
    phone = models.CharField('Zip Code', max_length=100)
    web = models.URLField(max_length=100)
    email_address = models.EmailField(max_length=100)

    def __str__(self):
        return self.name
    
class MyClubUser(models.Model):
    first_name = models.CharField(max_length=300)
    last_name = models.CharField(max_length=300)
    email_address = models.EmailField(max_length=100)

    def __str__(self):
        return self.first_name+' '+self.last_name

class Event(models.Model):
    name = models.CharField('Event Name', max_length=200)
    event_date = models.DateTimeField('Event Date')
    venue = models.ForeignKey(Venue, blank=True, null=True, on_delete=models.CASCADE)
    # venue = models.CharField(max_length=200)
    manager = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    attendees = models.ManyToManyField(MyClubUser, blank=True)

    def __str__(self):
        return self.name
    

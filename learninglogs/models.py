from django.db import models

# Create your models here.

class Topic(models.Model):
    """A topic a user is learning about"""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Returning a string representation of the model"""
        return self.text

    def print_date(self):
        print(self.date_added)

class Entry(models.Model):
    """Something specific learned about topic"""
    topic = models.ForeignKey(Topic)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        """Return a string representation of the model"""
        return self.text[:50] + "..."

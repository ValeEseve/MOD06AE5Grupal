from django.db import models

# Create your models here.
class Event(models.Model):
    header = models.CharField(max_length=200)
    description = models.TextField()
    location = models.CharField(max_length=200)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()

    def __str__(self):
        return f"{  self.header} - {self.date.strftime('%d-%m-%Y %H:%M') }"
    
class Assistant(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='assistants')

    def __str__(self):
        return f"{self.name} ({self.email}) - Evento: {self.event.header}"
from django.db import models

# Create your models here.
class Evento(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    fecha = models.DateTimeField()

    def __str__(self):
        return f"{  self.titulo} - {self.fecha.strftime('%d-%m-%Y %H:%M') }"
    
class Participante(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField()
    evento = models.ForeignKey(Evento, on_delete=models.CASCADE, related_name='participantes')

    def __str__(self):
        return f"{self.nombre} ({self.email}) - Evento: {self.evento.titulo}"
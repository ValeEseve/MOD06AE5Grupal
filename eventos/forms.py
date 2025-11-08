from django import forms
from eventos.models import Evento


class EventoForm(forms.ModelForm):
    class Meta:
        model = Evento
        fields = ['titulo', 'descripcion', 'fecha_inicio', 'fecha_fin', 'ubicacion']
        widgets = {
            'fecha_inicio': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'fecha_fin': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }

class ParticipanteForm(forms.Form):
    nombre = forms.CharField(max_length=100, label='Nombre')
    email = forms.EmailField(label='Correo Electrónico')
    evento = forms.ModelChoiceField(queryset=Evento.objects.all(), label='Evento')
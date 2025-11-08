from django import forms
from eventos.models import Event


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['header', 'description', 'location', 'start_date', 'end_date' ]
        widgets = {
            'start_date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'end_date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }

class ParticipanteForm(forms.Form):
    name = forms.CharField(max_length=100, label='Nombre')
    email = forms.EmailField(label='Correo Electrónico')
    event = forms.ModelChoiceField(queryset=Event.objects.all(), label='Event')
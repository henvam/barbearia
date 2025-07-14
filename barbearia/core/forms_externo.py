from django import forms
from .models import Agendamento

class AgendamentoPublicoForm(forms.ModelForm):
    class Meta:
        model = Agendamento
        fields = ['cliente', 'servico', 'data', 'hora']
        widgets = {
            'data': forms.DateInput(attrs={'type': 'date'}),
            'hora': forms.TimeInput(attrs={'type': 'time'}),
        }

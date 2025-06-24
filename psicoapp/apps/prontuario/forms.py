from django import forms
from .models import Prontuario
from apps.prescricoes.models import Prescricao
from apps.pacientes.models import Paciente

class ProntuarioForm(forms.ModelForm):
    class Meta:
        model = Prontuario
        fields = ['paciente', 'observacoes', 'prescricoes']
        widgets = {
            'observacoes': forms.Textarea(attrs={'rows': 4}),
            'prescricoes': forms.CheckboxSelectMultiple(),
        }

from django import forms
from .models import Profissional
from especialidades.models import Especialidade

class ProfissionalForm(forms.ModelForm):
    especialidade = forms.ModelChoiceField(
        queryset=Especialidade.objects.all(),
        label='Especialidade',
        required=True
    )
    registro_conselho = forms.CharField(
        max_length=50,
        label='Registro no Conselho',
        required=True
    )

    class Meta:
        model = Profissional
        fields = ['nome', 'email', 'telefone', 'especialidade', 'registro_conselho']

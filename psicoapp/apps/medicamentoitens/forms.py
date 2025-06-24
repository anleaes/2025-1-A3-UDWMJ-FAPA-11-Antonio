from django import forms
from .models import MedicamentoItem

class MedicamentoItemForm(forms.ModelForm):
    class Meta:
        model = MedicamentoItem
        fields = ['prescricao', 'medicamento', 'quantidade']
        widgets = {
            'prescricao': forms.Select(attrs={'class': 'form-control'}),
            'medicamento': forms.Select(attrs={'class': 'form-control'}),
            'quantidade': forms.NumberInput(attrs={'class': 'form-control'}),
        }

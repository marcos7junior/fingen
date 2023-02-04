from django import forms
from fingen.models import *

class TransacaoForm(forms.ModelForm):
    
    class Meta:
        model = Transacao
        fields = '__all__'

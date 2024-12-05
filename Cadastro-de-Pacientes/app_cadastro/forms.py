from django import forms
from .models import Trabajo

class TrabajoForm(forms.ModelForm):
    class Meta:
        model = Trabajo
        fields = [
            'numero_trabajo',
            'fecha_retiro',
            'es_cliente',
            'nombre_cliente',
            'domicilio',
            'telefono',
            'whatsapp',
            'email',
            'ojo_derecho_lejos_esf',
            'ojo_derecho_lejos_cil',
            'ojo_derecho_lejos_en',
            'ojo_derecho_lejos_dip',
            'ojo_izquierdo_lejos_esf',
            'ojo_izquierdo_lejos_cil',
            'ojo_izquierdo_lejos_en',
            'ojo_izquierdo_lejos_alt',
            'cristal_lejos',
            'armazon_lejos',
            'ojo_derecho_cerca_esf',
            'ojo_derecho_cerca_cil',
            'ojo_derecho_cerca_en',
            'ojo_derecho_cerca_dip',
            'ojo_izquierdo_cerca_esf',
            'ojo_izquierdo_cerca_cil',
            'ojo_izquierdo_cerca_en',
            'ojo_izquierdo_cerca_alt',
            'cristal_cerca',
            'armazon_cerca',
            'receta_doctor',
            'obra_social',
            'observaciones',
            'como_nos_conocio',
            'total',
            'seña',
            'saldo'
        ]
        widgets = {
            'fecha_retiro': forms.DateInput(attrs={'type': 'date'}),
            'fecha_dia': forms.DateInput(attrs={'type': 'date', 'readonly': 'true'}),
            'total': forms.NumberInput(attrs={'step': '0.01'}),
            'seña': forms.NumberInput(attrs={'step': '0.01'}),
            'saldo': forms.NumberInput(attrs={'step': '0.01'}),
        }

    def clean_total(self):
        total = self.cleaned_data.get('total')
        if total:
            return "{:,.2f}".format(total).replace(",", "X").replace(".", ",").replace("X", ".")
        return total

    def clean_seña(self):
        seña = self.cleaned_data.get('seña')
        if seña:
            return "{:,.2f}".format(seña).replace(",", "X").replace(".", ",").replace("X", ".")
        return seña

    def clean_saldo(self):
        saldo = self.cleaned_data.get('saldo')
        if saldo:
            return "{:,.2f}".format(saldo).replace(",", "X").replace(".", ",").replace("X", ".")
        return saldo
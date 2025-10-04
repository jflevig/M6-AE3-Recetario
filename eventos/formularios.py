from django import forms

# Importaciones para validación de fechas futuras
import datetime
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

# Función de validación de fechas futuras
def validate_future_date(value):
    if value <= datetime.date.today():
        raise ValidationError(_('La fecha no puede ser anterior a la actual.'))


class FormularioEvento(forms.Form):
    nombre_evento = forms.CharField(
        label='Nombre del Evento',
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        required=True
    )
    fecha_evento = forms.DateField(
        label='Fecha',
        widget=forms.SelectDateWidget(attrs={'class': 'form-select mb-2'}),
        validators=[validate_future_date],
        required=True
    )
    ubicacion = forms.CharField(
        label='Ubicación',
        max_length=150,
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        required=True
    )
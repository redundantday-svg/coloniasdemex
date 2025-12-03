from django import forms
from .models import Estado
from .models import municipio
from .models import colonia


class EstadoForm (forms.ModelForm):
    class Meta:
        model=Estado
        fields=['clave','nombre',]
class municipioForm (forms.ModelForm):
    class Meta:
        model=municipio
        fields=['nombre','estadop',]
class ColoniaForm (forms.ModelForm):
    class Meta:
        model=colonia
        fields=['nombre','municipio_p','codigo_p',]
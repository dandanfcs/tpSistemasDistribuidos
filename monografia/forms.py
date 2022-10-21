from django.db import models
from django.forms import ModelForm
from monografia.models import Autores, CoAutores, Discentes, Monografias

class AutoresForm(ModelForm):
    class Meta:
     model = Autores
     fields = ['nome','curso','universidade','email','lattes','g_scholar','linkedin','r_gate','orcid','github']


class CoAutoresForm(ModelForm):
    class Meta:
     model = CoAutores
     fields = ['nome','curso','universidade','email','lattes','g_scholar','linkedin','r_gate','orcid','github']


class DiscentesForm(ModelForm):
    class Meta:
     model = Discentes
     fields = ['nome','curso','universidade','email','lattes','g_scholar','linkedin','r_gate','orcid','github']


class MonografiasForm(ModelForm):
    class Meta:
     model = Monografias
     fields = ['titulo','autor','orientador','coorientador','data','resumo','palavrachave','universidade','curso','linkpdf']







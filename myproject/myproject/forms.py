from django.forms import ModelForm
from .model import jml_pelanggan

class DataForm(ModelForm):
    
    class Meta:
        model = jml_pelanggan
        fields = ['tanggal', 'pukul09', 'pukul10', 'pukul11', 'pukul12', 'pukul13', 'pukul14', 'pukul15', 'pukul16', 'pukul17', 'pukul18', 'pukul19', 'pukul20']
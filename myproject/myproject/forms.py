from django.forms import ModelForm
from .model import jml_pelanggan

class DataForm(ModelForm):
    
    class Meta:
        model = jml_pelanggan
        fields = ['tanggal', 'pukul_10', 'pukul_11', 'pukul_12', 'pukul_13', 'pukul_14', 'pukul_15', 'pukul_16', 'pukul_17', 'pukul_18', 'pukul_19', 'pukul_20', 'pukul_21']
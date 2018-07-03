from django.forms import ModelForm
from .model import rekap_pengunjung

class DataForm(ModelForm):
    
    class Meta:
        model = rekap_pengunjung
        fields = ['tanggal', 'pukul10', 'pukul11', 'pukul12', 'pukul13', 'pukul14', 'pukul15', 'pukul16', 'pukul17', 'pukul18', 'pukul19', 'pukul20', 'pukul21']
from django.db import models
# from django.utils import timezone

class jml_pelanggan(models.Model):
    # id = models.BigIntegerField()
    tanggal = models.CharField(primary_key=True)
    pukul09 = models.CharField(max_length=250)    
    pukul10 = models.CharField(max_length=250)
    pukul11 = models.CharField(max_length=250)
    pukul12 = models.CharField(max_length=250)
    pukul13 = models.CharField(max_length=250)
    pukul14 = models.CharField(max_length=250)
    pukul15 = models.CharField(max_length=250)
    pukul16 = models.CharField(max_length=250)
    pukul17 = models.CharField(max_length=250)
    pukul18 = models.CharField(max_length=250)
    pukul19 = models.CharField(max_length=250)
    pukul20 = models.CharField(max_length=250)
    
    class Meta:
        db_table="jml_pelanggan"
    
    def __unicode__(self):
        return self.tanggal
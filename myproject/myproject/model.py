from django.db import models
# from django.utils import timezone

class jml_pelanggan(models.Model):
    # id = models.BigIntegerField()
    tanggal = models.CharField(primary_key=True)
    pukul_10 = models.CharField(max_length=250)
    pukul_11 = models.CharField(max_length=250)
    pukul_12 = models.CharField(max_length=250)
    pukul_13 = models.CharField(max_length=250)
    pukul_14 = models.CharField(max_length=250)
    pukul_15 = models.CharField(max_length=250)
    pukul_16 = models.CharField(max_length=250)
    pukul_17 = models.CharField(max_length=250)
    pukul_18 = models.CharField(max_length=250)
    pukul_19 = models.CharField(max_length=250)
    pukul_20 = models.CharField(max_length=250)
    pukul_21 = models.CharField(max_length=250)
    
    class Meta:
        db_table="jml_pelanggan"
    
    def __unicode__(self):
        return self.tanggal
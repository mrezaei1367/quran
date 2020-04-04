from django.db import models

# Create your models here.

class Khatm(models.Model):
    # title = models.CharField(max_length=100, verbose_name="عنوان")
    joz=models.CharField(max_length=100 ,verbose_name="جز")
    hezb=models.CharField(max_length=100,verbose_name="حزب")
    selected=models.BooleanField(default=False,verbose_name="انتخاب شده")

    def __str__(self):
        return "{0} {1}".format(self.joz,self.hezb)

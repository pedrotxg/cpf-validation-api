from django.db import models
import os

class SociosCPF(models.Model):
    class Meta:
        verbose_name = "SociosCPF"
        verbose_name_plural = "SociosCPF"
        db_table = {os.getenv('TB_CLIENTE')}
    
    data_insercao = models.DateTimeField(auto_now_add=True)
    data_ultimo_update = models.DateTimeField(auto_now=True)

    col1 = models.CharField(max_length=30)
    col2 = models.CharField(max_length=10)
    cpf = models.CharField(max_length=11)
    
    def __str__(self):
        return f"CPF Sócio: {self.cpf}"
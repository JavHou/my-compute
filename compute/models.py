from django.db import models

# Create your models here.
class history(models.Model):
    sid=models.CharField(max_length=255,verbose_name="session id")
    history=models.CharField(max_length=255,verbose_name="计算历史")
    
    def __str__(self):
        return self.name
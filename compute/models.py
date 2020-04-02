from django.db import models

# Create your models here.


class User(models.Model):
    username = models.CharField(max_length=255, primary_key=True,verbose_name="用户名", unique=True)
    password = models.CharField(max_length=255, verbose_name="密码")

    # def __str__(self):
    #     return self.username

class History(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    history = models.CharField(max_length=255, verbose_name="计算历史", null=True)

    # def __str__(self):
    #     return self.username

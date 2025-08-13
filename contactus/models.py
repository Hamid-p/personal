from django.db import models

# Create your models here.
from django.db import models



class ContactUs(models.Model):
    name = models.CharField(max_length=150, verbose_name='نام')
    family = models.CharField(max_length=150, verbose_name='نام خانوادگی')
    email = models.EmailField(verbose_name='ایمیل')
    phone = models.CharField(max_length=20, verbose_name='تلفن')
    message = models.TextField(verbose_name='متن پیام')
    time = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'پیام'
        verbose_name_plural = 'پیام ها'

    def __str__(self):
        return self.name
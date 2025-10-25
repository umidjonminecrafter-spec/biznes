from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    ism = models.CharField(max_length=100, null=True, blank=True)
    familiyasi = models.CharField(max_length=100, null=True, blank=True)
    telefon = models.CharField(max_length=100, null=True, blank=True)
    tugilgan_sana = models.DateField(null=True, blank=True)
    yil = models.IntegerField(null=True, blank=True)
    manzil = models.CharField(max_length=100, null=True, blank=True)
    img = models.ImageField(upload_to='profile/', null=True, blank=True)
    role = models.CharField(max_length=100,choices=(('admin', 'Admin'), ('user','User')))

    def __str__(self):
        return self.user.username




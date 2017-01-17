from django.db import models
from django.utils import timezone
import random
import string

class MiniURL(models.Model):
    longUrl = models.URLField(verbose_name="URL à réduire", unique=True)
    code = models.CharField(unique=True, max_length=10)
    pseudo = models.CharField(blank=True, max_length=10)
    created_date = models.DateTimeField(verbose_name="Date d'enregistrement", default=timezone.now)
    access = models.IntegerField(verbose_name="Nombre d'accès à l'URL", default=0)

    def generer(self, nb_caracteres):
        caracteres = string.ascii_letters + string.digits
        aleatoire = [random.choice(caracteres) for _ in range(nb_caracteres)]
        return ''.join(aleatoire)

    def __str__(self):
        return self.longUrl
# Create your models here.

from django.db import models


class User(models.Model):
    email = models.EmailField()
    password = models.CharField('password', max_length=256)
    role = models.CharField('auth role', max_length=256)

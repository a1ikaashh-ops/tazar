from django.db import models
from django.conf import settings

class EcoPoint(models.Model):
    TYPE_CHOICES = [
        ('trash', 'Мусорная свалка'),
        ('water', 'Загрязнённая река'),
        ('forest', 'Вырубка леса'),
        ('air', 'Загрязнение воздуха'),
    ]

    STATUS_CHOICES = [
        ('active', 'Требует внимания'),
        ('resolved', 'Решено'),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField()
    type = models.CharField(max_length=20, choices=TYPE_CHOICES)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='active')
    photo = models.ImageField(upload_to='ecopoints/', blank=True, null=True)
    latitude = models.FloatField()
    longitude = models.FloatField()
    reported_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
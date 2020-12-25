from django.db import models
"""Працюємо з БД django"""
class Subscriber(models.Model):
    email = models.EmailField()
    name = models.CharField(max_length=256)

    def __str__(self):
        return 'Користувач %s %s' % (self.email, self.name)

    class Meta:
        verbose_name = 'MySubscriber'
        verbose_name_plural = 'A lot of Subscribers'

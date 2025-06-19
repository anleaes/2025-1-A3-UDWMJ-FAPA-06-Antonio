from django.db import models

# Create your models here.

class Fonte(models.Model):
    name = models.CharField('Nome', max_length=50)
    description = models.TextField('Descricao', max_length=100)
    url = models.URLField('URL', max_length=200, blank=True, null=True)
    
    class Meta:
        verbose_name = 'Fonte'
        verbose_name_plural = 'Fonte'
        ordering =['id']

    def __str__(self):
        return self.name
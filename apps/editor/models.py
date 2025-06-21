from django.db import models

# Create your models here.

class Editor(models.Model):
    name = models.CharField('Nome', max_length=50)
    email = models.EmailField('Email', max_length=50, blank=True, null=True)
    
    class Meta:
        verbose_name = 'Editor'
        verbose_name_plural = 'Editor'
        ordering =['id']

    def __str__(self):
        return self.name
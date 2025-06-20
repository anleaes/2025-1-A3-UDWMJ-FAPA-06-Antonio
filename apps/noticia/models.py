from django.db import models

# Create your models here.

class Noticia(models.Model):
    titulo = models.CharField('Titulo', max_length=50)
    conteudo = models.TextField('Conteudo', max_length=100)
    dataPublicacao = models.URLField('Data da Publicacao', max_length=200, blank=True, null=True)
    categoria = models.CharField('Categoria', max_length=50, blank=True, null=True)
    fonte = models.CharField('Fonte', max_length=50, blank=True, null=True)
    autor = models.CharField('Autor', max_length=50, blank=True, null=True)
    
    class Meta:
        verbose_name = 'Noticia'
        verbose_name_plural = 'Noticia'
        ordering =['id']

    def __str__(self):
        return self.name
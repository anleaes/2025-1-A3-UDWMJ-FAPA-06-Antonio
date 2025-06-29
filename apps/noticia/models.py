from django.db import models
from categories.models import Category
from fonte.models import Fonte
from autor.models import Autor

# Create your models here.

class Noticia(models.Model):
    titulo = models.CharField('Titulo', max_length=50)
    conteudo = models.CharField('Conteudo', max_length=500)
    dataPublicacao = models.DateField('Data da Publicacao', max_length=200, blank=True, null=True)
    noticia_category = models.ManyToManyField(Category, through='NoticiaCategoria', blank=True)
    fonte = models.ForeignKey(Fonte, on_delete=models.CASCADE, default=None, null=True, blank=True)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE, default=None, null=True, blank=True)
    
    class Meta:
        verbose_name = 'Noticia'
        verbose_name_plural = 'Noticias'
        ordering =['id']

    def __str__(self):
        return self.titulo
    
class NoticiaCategoria(models.Model):
    noticia = models.ForeignKey(Noticia, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Item de categoria'
        verbose_name_plural = 'Itens de categorias'
        ordering =['id']

    def str(self):
        return self.category.name
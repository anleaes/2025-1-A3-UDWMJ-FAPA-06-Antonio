from django.db import models
from editor.models import Editor
from noticia.models import Noticia


class Ndia(models.Model):
    editor = models.ForeignKey(Editor, on_delete=models.CASCADE)
    item_ndia = models.ManyToManyField(Noticia, through='ItemNdia', blank=True)

    class Meta:
        verbose_name = 'ndia'
        verbose_name_plural = 'ndia'
        ordering =['id']

    def str(self):
        return f"noticia de {self.editor.name}"


class ItemNdia(models.Model):
    ndia = models.ForeignKey(Ndia, on_delete=models.CASCADE)
    noticia = models.ForeignKey(Noticia, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Item ndia'
        verbose_name_plural = 'Item ndia'
        ordering =['id']

    def str(self):
        return self.noticia.titulo
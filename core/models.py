from django.db import models
from stdimage.models import StdImageField

# SIGNALS
from django.db.models import signals
from django.template.defaultfilters import slugify


# Criamos aqui uma classe abstrata, e esta não sera inserida no banco de dados

class Base(models.Model):
    criado = models.DateField('Data_de_criacao', auto_now_add=True)
    modificado = models.DateField('Data_de_Atualizacao', auto_now=True)
    ativo = models.BooleanField('Ativo', default=True)

    class Meta:
        abstract = True


class Produto(Base):
    nome = models.CharField('Nome', max_length=100)
    preco = models.DecimalField('Preco', max_digits=8, decimal_places=2)
    estoque = models.IntegerField('Estoque')
    imagem = StdImageField('Imagem', upload_to='produtos', variations={'thumb': (124, 124)})
    slug = models.SlugField('Slug', max_length=100, blank=True, editable=False)  # O Campo slug não pode ser editado

    def __str__(self):
        return self.nome


# Esta função vai realizar a tarefa de antes de salvar
def produto_pre_save(signal, instance, sender, **kwargs):
    instance.slug = slugify(instance.nome)


# Antes de salvar executa essa função aqui, quando o usuario submeter um produtopyt
signals.pre_save.connect(produto_pre_save, sender=Produto)

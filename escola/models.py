from django.db import models
from django.db import models
from django.utils import timezone

class BaseModelQuerySet(models.QuerySet):
    def delete(self):
        self.update(deleted_at=timezone.now() , is_active=False)
class BaseManager(models.Manager):
    def get_queryset (self):
        return BaseModelQuerySet( self.model, using=self._db).filter( deleted_at__isnull =True, is_active=True)

class BaseModel(models.Model):
    class Meta:
        abstract = True
    created_at =models.DateTimeField( auto_now_add =True)
    updated_at =models.DateTimeField( auto_now=True)
    deleted_at =models.DateTimeField( editable=False, blank=True, null=True)
    is_active = models.BooleanField( editable=False, default=True)
    objects = BaseManager()
    def delete(self, **kwargs):
        self.is_active = False
        self.deleted_at = timezone.now()
        self.save()
    def hard_delete (self, **kwargs):
        super(BaseModel, self).delete(**kwargs)

class Post(BaseModel):
    # ... seus outros campos ...
    title = models.CharField( max_length=200)
    content = models.TextField()
    pub_date = models.DateTimeField( auto_now_add =True)
    imagem = models.ImageField( upload_to='produtos/' , null=True, blank=True)

    def __str__(self):
        return self.title
    


# Projeto de Escola
# onde vou começar minhas classes
    
class Aluno(models.Model):
    nome = models.CharField(max_length=30)
    rg = models.CharField(max_length=9)
    cpf = models.CharField(max_length=11)
    dataNascimento = models.DateField()

    #para representar cada aluno pelo nome dele
    def __str__(self):
        return self.nome
    
class Curso(models.Model):

    # Criando uma constante chamada nivel
    NIVEL = (
        ('B', 'Básico'),
        ('I', 'Intermediário'),
        ('A', 'Avançado')
    )
    codigoCurso = models.CharField(max_length=10)
    descricao = models.CharField(max_length=100)
    nivel = models.CharField(max_length=1, choices=NIVEL, blank=False, null=False, default='B')

    #para representar cada descrição
    def __str__(self):
        return self.descricao
    
class Matricula(models.Model):
    PERIODO = (
        ('M', 'Matutino'),
        ('V', 'Vespertino'),
        ('N', 'Noturno')
    )
    # toda vez que um aluno for deletado, vai ser apagado a matricula dele e curso
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    periodo = models.CharField(max_length=1, choices=PERIODO, blank=False, null=False, default='M')

"""from django.db import models
from django.utils import timezone

class BaseModelQuerySet(models.QuerySet):
    def delete(self):
        self.update(deleted_at=timezone.now(), is_active=False)

class BaseManager(models.Manager):
    def get_queryset(self):
        return BaseModelQuerySet(self.model, using=self._db).filter(deleted_at__isnull=True, is_active=True)

class BaseModel(models.Model):
    class Meta:
        abstract = True
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(editable=False, blank=True, null=True)
    is_active = models.BooleanField(editable=False, default=True)
    objects = BaseManager()

    def delete(self, **kwargs):
        self.is_active = False
        self.deleted_at = timezone.now()
        self.save()

    def hard_delete(self, **kwargs):
        super(BaseModel, self).delete(**kwargs)

    class Meta:
        abstract = True

class Post(BaseModel):
    title = models.CharField(max_length=200)
    content = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    imagem = models.ImageField(upload_to='produtos/', null=True, blank=True)

    def __str__(self):
        return self.title

class Aluno(BaseModel):
    nome = models.CharField(max_length=30)
    rg = models.CharField(max_length=9)
    cpf = models.CharField(max_length=11)
    dataNascimento = models.DateField()

    def __str__(self):
        return self.nome

class Curso(BaseModel):
    NIVEL = (
        ('B', 'Básico'),
        ('I', 'Intermediário'),
        ('A', 'Avançado')
    )
    codigoCurso = models.CharField(max_length=10)
    descricao = models.CharField(max_length=100)
    nivel = models.CharField(max_length=1, choices=NIVEL, blank=False, null=False, default='B')

    def __str__(self):
        return self.descricao

class Matricula(BaseModel):
    PERIODO = (
        ('M', 'Matutino'),
        ('V', 'Vespertino'),
        ('N', 'Noturno')
    )
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    periodo = models.CharField(max_length=1, choices=PERIODO, blank=False, null=False, default='M')"""

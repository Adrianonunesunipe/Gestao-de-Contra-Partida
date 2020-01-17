from django.db import models

TURNO_CHOICES = [
    ('Manhã', 'Manhã'),
    ('Tarde', 'Tarde'),
    ('Noite', 'Noite'),
    ('Integral', 'Integral'),
]

CONCEDENTE_CHOICES = [
    ('Estado', 'Estado'),
    ('Municipio', 'Municipio'),
]


class Setor(models.Model):
    Setor = models.CharField(max_length=30, blank=True, default=None)

    def __str__(self):
        return self.Setor

    class Meta:
        verbose_name = 'Setor'
        verbose_name_plural = 'Setores'


class Convenio(models.Model):
    Concedente = models.CharField(choices=CONCEDENTE_CHOICES, null=False, blank=False, max_length=50)
    Razao_Social = models.CharField(max_length=50, blank=True, default=None, verbose_name="Razão Social")
    CNPJ = models.IntegerField(blank=True, default=None)
    Unidade_Executora = models.CharField(max_length=20, blank=True, default=None)
    Tipo_de_Estabelecimento = models.CharField(max_length=30, blank=True, default=None,
                                               verbose_name="Tipo de Estabelecimento")
    Representante = models.CharField(max_length=50, blank=True, default=None)
    Endereco = models.CharField(max_length=50, blank=True, default=None)
    Telefone = models.IntegerField(blank=True, default=None)
    Email = models.EmailField(max_length=30, blank=True, default=None)
    Descricao = models.CharField(max_length=100, default=None, blank=True, verbose_name="Descrição")
    Condicoes = models.CharField(max_length=100, default=None, blank=True, verbose_name="Condições")
    Data_Termino = models.DateField(max_length=30,default=None, blank=True, verbose_name='Data de Término')

    def __str__(self):
        return self.Razao_Social

    class Meta:
        verbose_name = 'Convênio'
        verbose_name_plural = 'Convênios'


class Curso(models.Model):
    Curso = models.CharField(max_length=30, blank=True, default=None)

    def __str__(self):
        return self.Curso


class Disciplina(models.Model):
    Curso = models.ForeignKey(Curso, default=None, on_delete=models.CASCADE)
    Nome = models.CharField(max_length=40, blank=True, default=None)
    Turno = models.CharField(choices=TURNO_CHOICES, null=False, blank=False, max_length=50)

    def __str__(self):
        return self.Nome


class Preceptor(models.Model):
    Nome = models.CharField(max_length=40, blank=True, default=None)
    Matricula = models.IntegerField(blank=True, default=None, verbose_name="Matrícula")
    Disciplina = models.ForeignKey(Disciplina, default=None, on_delete=models.CASCADE)

    def __str__(self):
        return self.Nome


class Local(models.Model):
    nome = models.CharField(max_length=30, blank=True, default=None)

    def __str__(self):
        return self.nome


class Estabelecimento(models.Model):
    tipo = models.CharField(max_length=30, blank=True, default=None)

    def __str__(self):
        return self.tipo


class Estagio(models.Model):
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, default=None)
    disciplina = models.ForeignKey(Disciplina, max_length=50, blank=True, default=None, on_delete=models.CASCADE)
    preceptor = models.ForeignKey(Preceptor, max_length=30, blank=True, default=None, on_delete=models.CASCADE)
    Tipo_de_Convenio = models.ForeignKey(Convenio, default=None, blank=True, on_delete=models.CASCADE,
                                         verbose_name="Concedente")
    Local = models.ForeignKey(Local, blank=True, default=None, on_delete=models.CASCADE)
    Tipo_de_Estabelecimento = models.ForeignKey(Estabelecimento, null=True, blank=True, default=None,
                                                on_delete=models.CASCADE, verbose_name="Tipo de Estabelecimento")
    Setor = models.CharField(max_length=50, blank=True, default=None)
    Quantidade_de_Alunos = models.IntegerField(blank=True, default=None)
    Turno = models.CharField(choices=TURNO_CHOICES, null=False, blank=False, max_length=50)
    Custo_por_Aluno = models.DecimalField(max_digits=5, decimal_places=2, blank=True, default=None)
    Data_Inicio = models.DateTimeField(verbose_name="Data de Início")
    Data_Termino = models.DateTimeField(verbose_name="Data de Término")
    Quantidade_de_Dias = models.IntegerField(default=None, blank=True)

    def __str__(self):
        return self.Local


def custo_total():
    v = 0
    z = 0
    x = 0
    tat = 0
    for i in Estagio.objects.all():
        c = i.Custo_por_Aluno
        v += c
        a = i.Quantidade_de_Dias
        z += a
        b = i.Quantidade_de_Alunos
        x += b
        tat += v * z * x
    return tat


def aluno():
    total = 0
    for i in Estagio.objects.all():
        tot = i.Quantidade_de_Alunos
        total += tot
        if custo_total() != 0:
            return custo_total() / total

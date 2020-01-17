from django.forms import ModelForm
from .models import Convenio, Estagio, Curso, Disciplina, Preceptor, Local, Estabelecimento


class ConvenioForm(ModelForm):
    class Meta:
        model = Convenio
        fields = ['Concedente', 'Endereco', 'Unidade_Executora', 'Tipo_de_Estabelecimento', 'Representante',
                  'Telefone', 'Email', 'Razao_Social', 'CNPJ', 'Condicoes', 'Descricao', 'Data_Termino']

    def __init__(self, *args, **kwargs):
        super(ConvenioForm, self).__init__(*args, **kwargs)
        self.fields['Razao_Social'].widget.attrs['placeholder'] = 'Razão Social'
        self.fields['Unidade_Executora'].widget.attrs['placeholder'] = 'Unidade Executora'
        self.fields['Endereco'].widget.attrs['placeholder'] = 'Endereço'
        self.fields['Tipo_de_Estabelecimento'].widget.attrs['placeholder'] = 'Tipo de Estabelecimento'
        self.fields['CNPJ'].widget.attrs['placeholder'] = 'CNPJ'
        self.fields['Representante'].widget.attrs['placeholder'] = 'Representante'
        self.fields['Concedente'].widget.attrs['placeholder'] = 'Concedente'
        self.fields['Telefone'].widget.attrs['placeholder'] = 'Telefone'
        self.fields['Email'].widget.attrs['placeholder'] = 'Email'
        self.fields['Descricao'].widget.attrs['placeholder'] = 'Descrição'
        self.fields['Condicoes'].widget.attrs['placeholder'] = 'Condições'


class EstagioForm(ModelForm):
    class Meta:
        model = Estagio
        fields = ['curso', 'disciplina', 'preceptor', 'Quantidade_de_Alunos',
                  'Custo_por_Aluno', 'Turno', 'Tipo_de_Convenio', 'Local',
                  'Tipo_de_Estabelecimento', 'Setor', 'Data_Inicio', 'Data_Termino', 'Quantidade_de_Dias']

    def __init__(self, *args, **kwargs):
        super(EstagioForm, self).__init__(*args, **kwargs)
        self.fields['preceptor'].widget.attrs['placeholder'] = 'Preceptor'
        self.fields['curso'].widget.attrs['placeholder'] = 'Curso'
        self.fields['Quantidade_de_Alunos'].widget.attrs['placeholder'] = 'Quantidade de Alunos'
        self.fields['Custo_por_Aluno'].widget.attrs['placeholder'] = 'R$'
        self.fields['Tipo_de_Convenio'].widget.attrs['placeholder'] = 'Convênio'
        self.fields['Local'].widget.attrs['placeholder'] = 'Local'
        self.fields['Tipo_de_Estabelecimento'].widget.attrs['placeholder'] = 'Tipo de Estabelecimento'
        self.fields['Setor'].widget.attrs['placeholder'] = 'Setor'
        self.fields['Quantidade_de_Dias'].widget.attrs['placeholder'] = 'Quantidade de Dias'
        self.fields['disciplina'].widget.attrs['placeholder'] = 'Disciplina'


class CursoForm(ModelForm):
    class Meta:
        model = Curso
        fields = ['Curso']

    def __init__(self, *args, **kwargs):
        super(CursoForm, self).__init__(*args, **kwargs)
        self.fields['Curso'].widget.attrs['placeholder'] = 'Nome do Curso'


class DisciplinaForm(ModelForm):
    class Meta:
        model = Disciplina
        fields = ['Nome', 'Turno', 'Curso']

    def __init__(self, *args, **kwargs):
        super(DisciplinaForm, self).__init__(*args, **kwargs)
        self.fields['Nome'].widget.attrs['placeholder'] = 'Nome'
        self.fields['Turno'].widget.attrs['placeholder'] = 'Turno'
        self.fields['Curso'].widget.attrs['placeholder'] = 'Curso'


class PreceptorForm(ModelForm):
    class Meta:
        model = Preceptor
        fields = ['Nome', 'Matricula', 'Disciplina']

    def __init__(self, *args, **kwargs):
        super(PreceptorForm, self).__init__(*args, **kwargs)
        self.fields['Nome'].widget.attrs['placeholder'] = 'Nome'
        self.fields['Matricula'].widget.attrs['placeholder'] = 'Matrícula'
        self.fields['Disciplina'].widget.attrs['placeholder'] = 'Disciplina'


class LocalForm(ModelForm):
    class Meta:
        model = Local
        fields = ['nome']

    def __init__(self, *args, **kwargs):
        super(LocalForm, self).__init__(*args, **kwargs)
        self.fields['nome'].widget.attrs['placeholder'] = 'Nome'


class EstabelecimentoForm(ModelForm):
    class Meta:
        model = Estabelecimento
        fields = ['tipo']

    def __init__(self, *args, **kwargs):
        super(EstabelecimentoForm, self).__init__(*args, **kwargs)
        self.fields['tipo'].widget.attrs['placeholder'] = 'Tipo de Estabelecimento'

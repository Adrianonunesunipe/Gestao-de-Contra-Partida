from django.shortcuts import render
from .models import Convenio, Estagio, Curso, Disciplina, Preceptor, Local, Estabelecimento, custo_total, aluno
from .forms import ConvenioForm, EstagioForm, CursoForm, DisciplinaForm, PreceptorForm, LocalForm, EstabelecimentoForm
from django.contrib.auth.decorators import login_required
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin


# Todas as classes que compõem o CRUD do sistema


class CursoCreate(LoginRequiredMixin, CreateView):
    model = Curso
    form_class = CursoForm
    template_name = 'curso_form.html'
    success_url = reverse_lazy('cursolista')


class CursoLista(LoginRequiredMixin, ListView):
    model = Curso
    template_name = 'curso_list.html'


def load_disciplinas(request):
    curso_id = request.GET.get('curso')
    cursos = Disciplina.objects.filter(Curso=curso_id)
    return render(request, 'disciplinas_dropdown_list.html', {'cursos': cursos})


class CursoUpdate(LoginRequiredMixin, UpdateView):
    model = Curso
    form_class = CursoForm
    template_name = 'curso_form_update.html'
    success_url = reverse_lazy('cursolista')


class CursoDelete(LoginRequiredMixin, DeleteView):
    model = Curso
    form_class = CursoForm
    template_name = 'curso_delete_form.html'
    success_url = reverse_lazy('cursolista')


class CursoDetail(LoginRequiredMixin, DetailView):
    model = Curso
    template_name = 'curso_detail.html'


class ConvenioCreate(LoginRequiredMixin, CreateView):
    model = Convenio
    form_class = ConvenioForm
    template_name = 'convenio_form.html'
    success_url = reverse_lazy('conveniolista')


class ConvenioList(LoginRequiredMixin, ListView):
    model = Convenio
    template_name = 'convenio_list.html'


class ConvenioDetail(DetailView):
    model = Convenio
    template_name = "convenio_detail.html"


class ConvenioUpdate(LoginRequiredMixin, UpdateView):
    model = Convenio
    form_class = ConvenioForm
    template_name = 'convenio_form_update.html'
    success_url = reverse_lazy('conveniolista')


class ConvenioDelete(LoginRequiredMixin, DeleteView):
    model = Convenio
    form_class = ConvenioForm
    template_name = 'convenio_delete_form.html'
    success_url = reverse_lazy('conveniolista')


class EstagioCreate(LoginRequiredMixin, CreateView):
    model = Estagio
    form_class = EstagioForm
    template_name = 'estagio_form.html'
    success_url = reverse_lazy('estagiolista')


class EstagioLista(LoginRequiredMixin, ListView):
    model = Estagio
    template_name = 'estagio_list.html'


class EstagioDetail(LoginRequiredMixin, DetailView):
    model = Estagio
    template_name = 'estagio_detail.html'


class EstagioUpdate(LoginRequiredMixin, UpdateView):
    model = Estagio
    template_name = 'estagio_form_update.html'
    form_class = EstagioForm
    success_url = reverse_lazy('estagiolista')


class EstagioDelete(LoginRequiredMixin, DeleteView):
    model = Estagio
    form_class = EstagioForm
    template_name = 'estagio_delete_form.html'
    success_url = reverse_lazy('estagiolista')


class DisciplinaCreate(LoginRequiredMixin, CreateView):
    model = Disciplina
    form_class = DisciplinaForm
    template_name = 'disciplina_form.html'
    success_url = reverse_lazy('disciplinalista')


class DisciplinaList(LoginRequiredMixin, ListView):
    model = Disciplina
    template_name = 'disciplina_list.html'


class DisciplinaUpdate(LoginRequiredMixin, UpdateView):
    model = Disciplina
    template_name = 'disciplina_form_update.html'
    form_class = DisciplinaForm
    success_url = reverse_lazy('disciplinalista')


class DisciplinaDelete(LoginRequiredMixin, DeleteView):
    model = Disciplina
    form_class = DisciplinaForm
    template_name = 'disciplina_delete_form.html'
    success_url = reverse_lazy('disciplinalista')


class DisciplinaDetail(LoginRequiredMixin, DetailView):
    model = Disciplina
    template_name = 'disciplina_detail.html'


class PreceptorCreate(LoginRequiredMixin, CreateView):
    model = Preceptor
    form_class = PreceptorForm
    template_name = 'preceptor_form.html'
    success_url = reverse_lazy('preceptorlista')


class PreceptorList(LoginRequiredMixin, ListView):
    model = Preceptor
    template_name = 'preceptor_list.html'


class PreceptorUpdate(LoginRequiredMixin, UpdateView):
    model = Preceptor
    template_name = 'preceptor_form_update.html'
    form_class = PreceptorForm
    success_url = reverse_lazy('preceptorlista')


class PreceptorDelete(LoginRequiredMixin, DeleteView):
    model = Preceptor
    form_class = PreceptorForm
    template_name = 'preceptor_delete_form.html'
    success_url = reverse_lazy('preceptorlista')


class PreceptorDetail(LoginRequiredMixin, DetailView):
    model = Preceptor
    template_name = 'preceptor_detail.html'


class LocalCreate(LoginRequiredMixin, CreateView):
    model = Local
    form_class = LocalForm
    template_name = 'local_form.html'
    success_url = reverse_lazy('listlocal')


class LocalList(LoginRequiredMixin, ListView):
    model = Local
    template_name = 'local_list.html'


class LocalUpdate(LoginRequiredMixin, UpdateView):
    model = Local
    template_name = 'local_form_update.html'
    form_class = LocalForm
    success_url = reverse_lazy('listlocal')


class LocalDelete(LoginRequiredMixin, DeleteView):
    model = Local
    form_class = LocalForm
    template_name = 'local_delete_form.html'
    success_url = reverse_lazy('listlocal')


class EstabelecimentoCreate(LoginRequiredMixin, CreateView):
    model = Estabelecimento
    form_class = EstabelecimentoForm
    template_name = 'Estabelecimento_form.html'
    success_url = reverse_lazy('listestabelecimento')


class EstabelecimentoList(LoginRequiredMixin, ListView):
    model = Estabelecimento
    template_name = 'Estabelecimento_list.html'


class EstabelecimentoUpdate(LoginRequiredMixin, UpdateView):
    model = Estabelecimento
    template_name = 'Estabelecimento_form_update.html'
    form_class = EstabelecimentoForm
    success_url = reverse_lazy('listestabelecimento')


class EstabelecimentoDelete(LoginRequiredMixin, DeleteView):
    model = Estabelecimento
    form_class = EstabelecimentoForm
    template_name = 'Estabelecimento_delete_form.html'
    success_url = reverse_lazy('listestabelecimento')


@login_required
def dash_board(request):
    estagios = Estagio.objects.all()
    return render(request, 'dashboard.html', {'estagios': estagios, 'q': custo_total(), 'media': aluno()})

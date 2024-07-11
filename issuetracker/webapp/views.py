from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView

from .forms import IssueForm
from .models import Issue, Status, Type


class IssueListView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['issues'] = Issue.objects.all()
        return context

class IssueCreateView(CreateView):
    template_name = 'issue_create.html'
    form_class = IssueForm
    success_url = reverse_lazy('issue_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['statuses'] = Status.objects.all()
        context['types'] = Type.objects.all()
        return context
class IssueDetailView(TemplateView):
    template_name = 'issue_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.kwargs['pk']
        context['issue'] = Issue.objects.get(pk=pk)
        return context

class IssueUpdateView(TemplateView):
    template_name = 'issue_edit.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.kwargs['pk']
        context['issue'] = Issue.objects.get(pk=pk)
        return context

class IssueDeleteView(TemplateView):
    template_name = 'issue_delete.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.kwargs['pk']
        context['issue'] = Issue.objects.get(pk=pk)
        return context

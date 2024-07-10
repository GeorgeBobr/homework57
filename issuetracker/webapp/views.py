from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Issue
from .forms import IssueForm

class IssueListView(ListView):
    model = Issue
    template_name = 'index.html'

class IssueDetailView(DetailView):
    model = Issue
    template_name = 'issue_detail.html'

class IssueCreateView(CreateView):
    model = Issue
    form_class = IssueForm
    template_name = 'issue_create.html'
    success_url = reverse_lazy('index')

class IssueUpdateView(UpdateView):
    model = Issue
    form_class = IssueForm
    template_name = 'issue_edit.html'
    success_url = reverse_lazy('index')

class IssueDeleteView(DeleteView):
    model = Issue
    template_name = 'issue_delete.html'
    success_url = reverse_lazy('index')

from django.urls import path
from django.views.generic import RedirectView
from .views import IssueListView, IssueCreateView, IssueDetailView, IssueUpdateView, IssueDeleteView

urlpatterns = [
    path('issues/', IssueListView.as_view(), name='index'),
    path('', RedirectView.as_view(pattern_name='index')),
    path('issue/create/', IssueCreateView.as_view(), name='issue_create'),
    path('issue/<int:pk>/', IssueDetailView.as_view(), name='issue_detail'),
    path('issue/<int:pk>/update/', IssueUpdateView.as_view(), name='issue_update'),
    path('issue/<int:pk>/delete/', IssueDeleteView.as_view(), name='issue_delete'),
]

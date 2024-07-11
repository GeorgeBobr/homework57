from django import forms
from django.forms import widgets

from webapp.models import Type


class IssueForm(forms.Form):
    title = forms.CharField(max_length=3, required=True, label="Название")
    author = forms.CharField(
        max_length=50,
        required=False,
        label="Автор",
        initial="Неизвестный",
        widget=widgets.Input(attrs={"placeholder": "Автор"}),
    )
    content = forms.CharField(
        max_length=3000,
        required=True,
        label="Контент",
        widget=widgets.Textarea(attrs={"cols": 20, "rows": 5, "placeholder": "Контент"}),
    )
    types = forms.ModelChoiceField(queryset=Type.objects.all(), required=True)

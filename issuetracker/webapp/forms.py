from django import forms
from .models import Issue, Status, Type

class IssueForm(forms.ModelForm):
    class Meta:
        model = Issue
        fields = ['summary', 'description', 'status', 'types']
        widgets = {
            'summary': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'status': forms.Select(attrs={'class': 'form-control'}),
            'types': forms.SelectMultiple(attrs={'class': 'form-control', 'size': 5}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['status'].queryset = Status.objects.all()
        self.fields['types'].queryset = Type.objects.all()

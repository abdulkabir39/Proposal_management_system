from django import forms
from .models import Proposal  

class ProposalForm(forms.ModelForm):
    class Meta:
        model = Proposal  
        fields = ['title', 'proposal_type', 'file']

    title = forms.CharField(
        widget=forms.TextInput(attrs={
            'id': 'proposal-title',
            'placeholder': 'Enter the proposal title',
            'class': 'form-group',
            'required': True
        })
    )

    PROPOSAL_TYPES = [
        ('', 'Select a type'),
        ('Research', 'Research'),
        ('Business', 'Business'),
        ('Grant', 'Grant'),
    ]

    proposal_type = forms.ChoiceField(
        choices=PROPOSAL_TYPES,
        widget=forms.Select(attrs={
            'id': 'proposal-type',
            'class': 'form-group',
            'required': True
        })
    )

    file = forms.FileField(
        widget=forms.FileInput(attrs={
            'id': 'proposal-upload',
            'accept': '.pdf,.doc,.docx,.txt',
            'class': 'form-group',
            'required': True
        })
    )

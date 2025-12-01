from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'budget', 'message']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'block w-full rounded-md border-gray-700 bg-neutral-900 text-gray-200 shadow-sm focus:border-cyan-400 focus:ring-cyan-400',
            }),
            'email': forms.EmailInput(attrs={
                'class': 'block w-full rounded-md border-gray-700 bg-neutral-900 text-gray-200 shadow-sm focus:border-cyan-400 focus:ring-cyan-400',
            }),
            'budget': forms.Select(attrs={
                'class': 'rounded-lg border border-slate-200 p-3 text-sm focus:outline-none focus:ring-2 focus:ring-indigo-300 bg-neutral-900 text-gray-200',
            }),
            'message': forms.Textarea(attrs={
                'rows': 5,
                'class': 'block w-full rounded-md border-gray-700 bg-neutral-900 text-gray-200 shadow-sm focus:border-cyan-400 focus:ring-cyan-400',
            }),
        }
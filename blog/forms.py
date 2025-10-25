from django.forms import ModelForm
from .models import Email,Comment
        # blog/forms.py
from django import forms


class EmailForm(ModelForm):
    class Meta:
        model = Email
        fields = '__all__'


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
        widgets = {
            'text': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Izoh qoldiring...'
            }),
        }
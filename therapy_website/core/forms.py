from django import forms
from django.core.validators import RegexValidator


class ContactForm(forms.Form):
    name = forms.CharField(
        max_length=100,
        label='',
        widget=forms.TextInput(attrs={'placeholder': 'Name'})
    )
    email = forms.EmailField(
        label='',
        widget=forms.EmailInput(attrs={'placeholder': 'Email'})
    )
    phone_number = forms.CharField(
        max_length=15,
        required=False,
        label='',
        validators=[
            RegexValidator(
                regex=r'^(0|\+44)\d{10}$',
                message="Phone number must start with 0 or +44."
            )
        ],
        widget=forms.TextInput(attrs={'placeholder': 'Phone Number (optional)'})
    )
    message = forms.CharField(
        label='',
        widget=forms.Textarea(attrs={'placeholder': 'Your Message'})
    )

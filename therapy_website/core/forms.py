from django import forms
from django.core.validators import RegexValidator


class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    phone_number = forms.CharField(
        max_length=15,
        required=False,
        validators=[
            RegexValidator(
                regex=r'^(0|\+44)\d{10}$',
                message="Phone number must start with 0 or +44."
            )
        ]
    )
    message = forms.CharField(widget=forms.Textarea)

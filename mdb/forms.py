from django import forms
from django.core.exceptions import ValidationError

def is_too_easy(value):
    if value == '1234':
        raise ValidationError('Is too easy')
    return value

class SimpleForm(forms.Form):
    password = forms.CharField(max_length=15, validators=[is_too_easy, ])
    password2 = forms.CharField(max_length=15)
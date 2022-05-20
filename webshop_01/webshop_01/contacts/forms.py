from django import forms
from webshop_01 import constants


class ContactForm(forms.Form):
    first_name = forms.CharField(
        max_length=constants.CHAR_FIELD_DEFAULT_MAX_LEN,
        widget=forms.TextInput(
            attrs={'class': 'form-control mt-1', 'placeholder': 'Name'}
        )
    )
    email = forms.EmailField(
        max_length=constants.CHAR_FIELD_DEFAULT_MAX_LEN,
        widget=forms.EmailInput(
            attrs={'class': 'form-control mt-1', 'placeholder': 'Email'}
        )
    )
    subject = forms.CharField(
        max_length=constants.CHAR_FIELD_DEFAULT_MAX_LEN,
        widget=forms.TextInput(
            attrs={'class': 'form-control mt-1', 'placeholder': 'Subject'}
        )
    )
    message_content = forms.CharField(
        max_length=constants.TEXT_FIELD_DEFAULT_MAX_LEN,
        widget=forms.Textarea(
            attrs={
                'rows': 5,
                'class': 'form-control mt-1',
                'placeholder': 'Message',
            },
        )
    )


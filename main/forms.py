from django import forms


class GuestForm(forms.Form):
    name = forms.CharField(label='Imię: ', max_length='30')
    surname = forms.CharField(label='Nazwisko: ', max_length='30')
    bus = forms.BooleanField()
    overnight = forms.BooleanField()
    comments = forms.CharField(label='Comments')

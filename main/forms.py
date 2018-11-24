from django import forms


class GuestForm(forms.Form):
    name = forms.CharField(label='Imię: ', max_length='30')
    surname = forms.CharField(label='Nazwisko: ', max_length='30')
    bus = forms.CheckboxInput()
    overnight = forms.CheckboxInput()
    commments = forms.CharField(label='Comments')

    def get_name_and_surname(self):
        return self.name, self.surname

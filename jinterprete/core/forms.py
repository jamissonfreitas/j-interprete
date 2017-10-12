from django import forms


class InterpreteForm(forms.Form):
    interprete_file = forms.FileField()
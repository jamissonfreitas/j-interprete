from django import forms


class InterpreteForm(forms.Form):
    LANGUAGE_CHOICE = (
        ('por', "POR"),
        ('eng', "ENG"),
    )

    interprete_file = forms.FileField()
    language = forms.ChoiceField(choices=LANGUAGE_CHOICE)
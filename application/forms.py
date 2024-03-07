from django import forms


class BaseballForms(forms.Form):
    player = forms.CharField(required=False)
    team = forms.CharField(required=False)
    year = forms.CharField(required=False)
#
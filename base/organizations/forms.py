from django import forms

class FilterForm(forms.Form):
    tag = forms.CharField(max_length=20, required=False)
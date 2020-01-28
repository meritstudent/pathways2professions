from django import forms

import re
all_tags = [
    (0, "transportation"),
    (1, "stuff"),
    (2, "more stuff"),
    (3, "even more stuff")
]

class FilterForm(forms.Form):
    # tag = forms.CharField(max_length=20)

    tag = forms.ChoiceField(label="tags", required=True, choices=all_tags)
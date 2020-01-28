from django import forms

all_tags = [
    (0, "transportation"),
    (1, "stuff"),
    (2, "more stuff"),
    (3, "even more stuff")
]

from .models import Tag
db_AllTags = Tag.objects.all()
# all_tags

class FilterForm(forms.Form):
    # tag = forms.CharField(max_length=20)

    tags = forms.MultipleChoiceField(label="tags", required=True, choices=all_tags)
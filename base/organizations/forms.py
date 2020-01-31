from django import forms
from .models import Tag

all_tags = []
db_tags = Tag.objects.all()
for i in range(len(db_tags)):
    all_tags.append((i, db_tags[i].CTE_area))


db_AllTags = Tag.objects.all()
# all_tags

class FilterForm(forms.Form):
    # tag = forms.CharField(max_length=20)
    favorites = forms.BooleanField(required=False)
    tags = forms.MultipleChoiceField(label="tags", required=False, choices=all_tags, widget=forms.CheckboxSelectMultiple,)
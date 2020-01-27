from django.shortcuts import render
from .organizations.forms import FilterForm
from .organizations.models import Organization, OTRelation, Tag

# Create your views here.
def index(request):
    return render(request, template_name="index.html")

def map_view(request):
    return render(request, template_name="map.html")

def about(request):
    return render(request, template_name="about.html")


def organizations(request):

    if request.method == 'POST':
        form = FilterForm(request.POST)

        if form.is_valid():
            # get Tags from database
            tags = Tags.objects.filter(CTE_area=form.form.cleaned_data['tag'])
            # get OTRelations using Tags
            OTRelations = []
            # TODO: get multiple tags at once
            for tag in tags:
                OTRelations.append( OTRelation.objects.filter(_tag=tag) )
            # get Organizations using OTRelations

            # get Organizations using cached favorites
            # add Organizations to a list
            # render with Organizations list

            pass
        

    return render(request, template_name="organizations.html")
    

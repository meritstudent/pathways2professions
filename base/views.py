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

def external(request):
    pass


def organizations(request):
    filter_form =FilterForm()
    if request.method == 'POST':
        form = FilterForm(request.POST)

        if form.is_valid():
            # get Tags from database
            tags = Tag.objects.filter(CTE_area= form.cleaned_data['tag']).get()
            # get OTRelations using Tags
            OTRelations = OTRelation.objects.filter(_tag=tags)
            # get Organizations using OTRelations
            organizations = []
            for relation in OTRelations:
                organizations.append(relation._org)

            # TODO: get Organizations using cached favorites
            # add Organizations to a list with displayed values
            orgs = []
            for org in organizations:
                if not "https://" in org.link and not "http://" in org.link:
                    org.link = "https://" + org.link
                orgs.append({
                    'name': org.name,
                    'link': org.link,
                    'description': org.description,
                    'location': org.location
                })
            # render with Organizations list
            return render(request,
                            template_name="organizations.html",
                            context={
                                'orgs': orgs,
                                'filter': filter_form,
                            })
    
    orgs = Organization.objects.all()
        
        

    return render(request, 
                    template_name="organizations.html",
                    context={ 
                        'orgs': orgs,
                        'filter': filter_form
                        })
    

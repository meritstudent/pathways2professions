from django.shortcuts import render
from .organizations.forms import FilterForm, all_tags
from .organizations.models import Organization, OTRelation, Tag
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, template_name="index.html")

def map_view(request):
    return render(request, template_name="map.html")

def about(request):
    return render(request, template_name="about.html")


def organizations(request):
    form = FilterForm(request.POST)
    if request.method == 'POST':
        # form = FilterForm(request.POST)

        if form.is_valid():
            # get Tags from database
            select = form.cleaned_data['tags']
            select_str = []

            for tag in select:
                select_str.append( all_tags[int(tag)][1] )

            # adding __in lets it use a list
            tags = Tag.objects.filter(CTE_area__in= select_str )
            # get OTRelations using Tags
            OTRelations = OTRelation.objects.filter(_tag__in=tags)
            # get Organizations using OTRelations

            organizations = []
            favorites = []
            # import pdb 
            # pdb.set_trace
            try:
                favorites = Organization.objects.filter(id__in=request.session["favorites"])
            except:
                pass
    

            if form.cleaned_data['favorites']:
                for favorite in favorites:
                    organizations.append(favorite)

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
                    'location': org.location,
                    'id': org.id
                })
            # render with Organizations list
            return render(request,
                            template_name="organizations.html",
                            context={
                                'orgs': orgs,
                                'filter': form,
                                'favorites': request.session["favorites"],
                            })
    
    orgs = Organization.objects.all()
        
        

    return render(request, 
                    template_name="organizations.html",
                    context={ 
                        'orgs': orgs,
                        'filter': form,
                        'favorites': request.session["favorites"],
                        })
    

def toggle(request):
    import pdb; pdb.set_trace()
    try:
        favorites_list = request.session["favorites"]
        if (request.POST['favorite']== "true") :
            favorites_list.append( request.POST['id'] )
        else:
            favorites_list.remove( request.POST['id'] )

        request.session["favorites"]=favorites_list
    except:
        favorites_list =[]
        favorites_list.append( request.POST['id'] )

        request.session["favorites"]=favorites_list

    return HttpResponse('success')
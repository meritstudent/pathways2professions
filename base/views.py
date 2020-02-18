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

    favorite_list =[]
    try:
        favorite_list = request.session["favorites"]
        favorite_list = [int(i) for i in favorite_list]
    except:
        pass
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

            # get Organizations using cached favorites
            organizations = []
            favorites = []
            try:
                favorites = Organization.objects.filter(id__in=request.session["favorites"]).order_by("name")
            except:
                pass

            if form.cleaned_data['favorites']:
                for favorite in favorites:
                    if not favorite in organizations:
                        organizations.append(favorite)
            

            # get Organizations using OTRelations
            for relation in OTRelations:
                if not relation._org in organizations:
                    organizations.append(relation._org)
            
            # if there are no active filters get all organizations
            if not tags:
                if not form.cleaned_data['favorites']:
                    organizations = Organization.objects.all().order_by("name")
            
            

            # add Organizations to a list with displayed values
            orgs = []
            for org in organizations:

                # get relations
                relations = OTRelation.objects.filter(_org= org)
                # get tags
                org_tags = []
                for relation in relations:
                    org_tags.append(relation._tag)
                

                if not "https://" in org.link and not "http://" in org.link:
                    org.link = "https://" + org.link
                orgs.append({
                    'name': org.name,
                    'link': org.link,
                    'description': org.description,
                    'location': org.location,
                    'id': org.id,
                    'tags': org_tags
                })

            # render with Organizations list
            return render(request,
                template_name="organizations.html",
                context={
                    'orgs': orgs,
                    'filter': form,
                    'favorites': favorite_list,
                    'hide_filter': True
                })
    
    ############################## when not filtered #####################################
    orgs =[]
    organizations = Organization.objects.all().order_by("name")
    for org in organizations:
        # get relations
        relations = OTRelation.objects.filter(_org= org)
        # get tags
        org_tags = []
        for relation in relations:
            org_tags.append(relation._tag)


        if not "https://" in org.link and not "http://" in org.link:
            org.link = "https://" + org.link
        orgs.append({
            'name': org.name,
            'link': org.link,
            'description': org.description,
            'location': org.location,
            'id': org.id,
            'tags': org_tags
        })
        

    return render(request, 
        template_name="organizations.html",
        context={ 
            'orgs': orgs,
            'filter': form,
            'favorites': favorite_list,
            'hide_filter': False
        })
    

def toggle(request):
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
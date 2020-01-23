from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, template_name="index.html")

def map_view(request):
    return render(request, template_name="map.html")

def about(request):
    return render(request, template_name="about.html")


def organizations(request):

    # if request.method == 'POST':
        

    return render(request, template_name="organizations.html")
    

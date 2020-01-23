from django.urls import path, include

from django.contrib import admin
from django.views.generic import TemplateView

from .views import home, organizations, map_view, about

admin.autodiscover()

# To add a new path, first import the app:
# import blog
#
# Then add the new path:
# path('blog/', blog.urls, name="blog")
#
# Learn more here: https://docs.djangoproject.com/en/3.0/topics/http/urls/


urlpatterns = [
    path("", TemplateView.as_view(template_name="index.html"), name="index"),
    path("/admin/", admin.site.urls),

    path('organizations', organizations, name="organizations"),
    path('map', map_view, name="map"),
    path('about', about, name="about"),
]

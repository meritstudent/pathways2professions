from django.contrib import admin
from .models import Organization, OTRelation, Tag

# Register your models here.
admin.site.register(Organization)
admin.site.register(Tag)
admin.site.register(OTRelation)
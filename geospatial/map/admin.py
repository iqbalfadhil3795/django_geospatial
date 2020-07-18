from leaflet.admin import LeafletGeoAdmin
from django.contrib import admin

from . import models as map


admin.site.register(map.Map, LeafletGeoAdmin)

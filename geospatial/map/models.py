# from djgeojson.fields import PolygonField
from django.db import models
from django.contrib.gis.db import models as gis_models
from django.contrib.gis.geos import Point, Polygon
from django.conf import settings


class Map(models.Model):
    title = models.CharField(max_length=256)
    description = models.TextField()
    picture = models.ImageField()
    geom = gis_models.PolygonField()

    def __str__(self):
        return self.title

    @property
    def picture_url(self):
        return self.picture.url

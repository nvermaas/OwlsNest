from django.db import models
#from django.core.urlresolvers import reverse
from django.urls import reverse
import re

# Create your models here.
class Hike(models.Model):
    title = models.CharField(max_length=100)
    place = models.CharField(max_length=40)
    country = models.CharField(max_length=20)
    date = models.CharField(max_length=20)
    year = models.IntegerField(default=2000)
    duration = models.CharField(max_length=20)
    hike_image_url = models.URLField(max_length=250, default='',blank=True)
    visible = models.IntegerField(default=1)
    description = models.TextField(max_length=3000, blank=True)

    def get_absolute_url(self):
        return reverse('hiking:details', kwargs={'pk': self.pk})

    def __str__(self):
        return self.title + ' - ' + str(self.year) + ' - '+ self.country + ' - ' + self.place

    def get_year(self):
        #scan for 4 digits
        match = re.search(r'\d{4}', self.date)
        return int(match.group())

    @property
    def link_to_gallery(self):
        try:
            q = TripDetail.objects.filter(hike=self).filter(kind='gallery')[0].details_url
        except:
            q = None
        return q

    @property
    def link_to_movie(self):
        try:
            q = TripDetail.objects.filter(hike=self).filter(kind='movie')[0].details_url
        except:
            q = None
        return q

    @property
    def link_to_map(self):
        try:
            q = TripDetail.objects.filter(hike=self).filter(kind='map')[0].details_url
        except:
            q = None
        return q

    @property
    def link_to_report(self):
        try:
            q = TripDetail.objects.filter(hike=self).filter(kind='report')[0].details_url
        except:
            q = None
        return q

class TripDetail(models.Model):
    KIND_IMAGE = 'image'
    KIND_MOVIE = 'movie'
    KIND_LINK = 'link'
    KIND_OTHER = 'other'
    KIND_GALLERY = 'gallery'
    KIND_MAP = 'map'

    KIND_CHOICES = (
        (KIND_IMAGE, 'Image'),
        (KIND_MOVIE, 'Movie'),
        (KIND_LINK, 'Link'),
        (KIND_GALLERY, 'Gallery'),
        (KIND_OTHER, 'Other'),
        (KIND_MAP, 'Map'),
    )

    # use the Meta class to order the TripDetails (inside the Hike)
    class Meta:
        ordering = ['order']

    # hike = models.ForeignKey(Hike, related_name='trip_details', on_delete=models.CASCADE)
    hike = models.ForeignKey(Hike, on_delete=models.CASCADE)
    title =  models.CharField(max_length=50, blank=True)
    description = models.TextField(max_length=3000, blank=True)
    details_url = models.URLField(max_length=250, default='',blank=True)
    # kinds : image, movie
    kind = models.CharField(max_length=30, choices=KIND_CHOICES, default=KIND_IMAGE)
    order = models.IntegerField(default=0)
    visible = models.IntegerField(default=1)

    def get_absolute_url(self):
        return reverse('hiking:details', kwargs={'pk': self.pk})

    def __str__(self):
        return self.title + ' - ' + self.description


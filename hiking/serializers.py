from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Hike, TripDetail

class HikeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Hike
        fields = ('id','title','place','country','date','year','duration','hike_image_url','visible')

class TripDetailSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TripDetail
        fields = ('hike', 'title', 'description', 'kind', 'details_url','order','visible')

from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Hike, TripDetail

class HikeSerializer(serializers.HyperlinkedModelSerializer):
    # this adds a 'trip_details' list with hyperlinks to the Hike resource.
    # note that 'trip_details' relationship is not defined in the TripDetails model, but in the Hike model.
    #trip_details = serializers.HyperlinkedRelatedField(
    #    many=True,
    #    read_only=True,
    #    # queryset=Process.objects.all(),
    #    view_name='details',
    #    lookup_field='pk'
    #)

    class Meta:
        model = Hike
        fields = ('id','title','place','country','date','year','duration','hike_image_url','visible')

class TripDetailSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = TripDetail
        fields = ('id','hike_id','title', 'description', 'kind', 'details_url','order','visible')


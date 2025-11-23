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
        fields = "__all__"


class TripDetailSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = TripDetail
        fields = "__all__"


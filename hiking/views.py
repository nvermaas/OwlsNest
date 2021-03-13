

from django.shortcuts import render, redirect

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.reverse import reverse
from rest_framework import generics

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from django.views import generic

from .models import Hike, TripDetail
from .serializers import HikeSerializer, TripDetailSerializer
from django.db.models import Q
from . import config

# constants, read from a config later

# --- REST API ---

# --- REST API ---

class HikeListAPI(generics.ListCreateAPIView):
    """
    List all Hikes, or create a new Hike.
    """
    queryset = Hike.objects.order_by('-year','-id')
    serializer_class = HikeSerializer

class HikeDetailsAPI(generics.RetrieveUpdateDestroyAPIView):
    """
    List all TripDetails, or create a new TripDetail
    """
    queryset = Hike.objects.all()
    serializer_class = HikeSerializer

class TripDetailsListAPI(generics.ListCreateAPIView):
    """
    List all Hikes, or create a new Hike.
    """
    queryset = TripDetail.objects.all()
    serializer_class = TripDetailSerializer


class TripDetailsDetailsAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = TripDetail.objects.all()
    serializer_class = TripDetailSerializer

# --- GUI ---

class IndexView(generic.ListView):
    template_name = 'hiking/index.html'

    # by default this returns the list in an object called object_list, so use 'object_list' in the html page.
    # but if 'context_object_name' is defined, then this returned list is named and can be accessed that way in html.
    context_object_name = 'my_hikes_all'

    def get_queryset(self):
        hike_list = Hike.objects.all().order_by('-year','-id')

        search_box = self.request.GET.get('search_box', None)
        if (search_box is not None):
            hike_list = get_searched_hikes(search_box)

        paginator = Paginator(hike_list, config.HIKES_PER_PAGE)  # Show x hikes per page
        page = self.request.GET.get('page')

        try:
            hikes = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            hikes = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            hikes = paginator.page(paginator.num_pages)

        return hikes

def get_searched_hikes(q):
    hikes = Hike.objects.filter(
        Q(title__contains=q) |
        Q(place__contains=q) |
        Q(year__contains=q) |
        Q(country__contains=q)).order_by('-year')
    return hikes


class DetailsView(generic.DetailView):
    model = Hike
    # by default this would be 'hike_detail.html', but 'template_name' overrides the default name.
    template_name = 'hiking/details.html'
    serializer_class = TripDetailSerializer




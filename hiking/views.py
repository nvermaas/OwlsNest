from datetime import datetime
from django.shortcuts import render, redirect
from rest_framework import generics
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views import generic

from .models import Hike, TripDetail
from .serializers import HikeSerializer, TripDetailSerializer
from django.db.models import Q
from . import config

# constants, read from a config later

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
    context_object_name = 'selected_hikes'

    def get_queryset(self):
        hike_list = Hike.objects.all().order_by('-date')

        # check if there is a 'task_filter' put on the session
        try:
            filter = self.request.session['hike_filter']
            if filter!='all':
                hike_list = get_searched_hikes(filter)
        except:
            pass

        search_box = self.request.GET.get('search_box', None)
        if (search_box is not None):
            hike_list = get_searched_hikes(search_box)

        hike_list = hike_list.filter(visible=1)
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
        Q(title__icontains=q) |
        Q(place__icontains=q) |
        Q(year__icontains=q) |
        Q(country__icontains=q)).order_by('-date')
    return hikes


class DetailsView(generic.DetailView):
    model = Hike
    # by default this would be 'hike_detail.html', but 'template_name' overrides the default name.
    template_name = 'hiking/details.html'
    serializer_class = TripDetailSerializer

    def get_context_data(self, **kwargs):
        # Get the default context from DetailView
        context = super().get_context_data(**kwargs)

        hike = self.object

        # Add extra context
        # convert the hike.date to something human readable
        year, month_str = hike.date.split("_")
        # If month_str has more than 1 digit, ignore the last digit
        if len(month_str) > 2:
            month_str = month_str[:-1]
        month = int(month_str)
        dt = datetime(int(year), month, 1)
        formatted = dt.strftime("%B %Y")

        #days = f", {hike.days} days" if hike.days else ""
        with_who = f", with {hike.with_who}" if hike.with_who else ""
        #kilometers = f", {hike.kilometers} km" if hike.kilometers else ""

        context['subtitle'] = f'{formatted}{with_who}'

        return context

# set a filter value in the session, used later by the 'get_searched_tasks' mechanism
def HikeSetFilter(request,filter):
    request.session['hike_filter'] = filter
    return redirect('hiking:index')


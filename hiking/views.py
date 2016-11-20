from django.shortcuts import render, get_object_or_404

from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.http import Http404

from rest_framework import viewsets
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.reverse import reverse
from rest_framework import mixins
from rest_framework import generics

from django.http import HttpResponse

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from django.views import generic
from django.views.generic import View
from .models import Hike, TripDetail
from .forms import myLoginForm,myRegisterForm, myContactForm
from .serializers import HikeSerializer, TripDetailSerializer

from .static.hiking import config

# constants, read from a config later

# --- REST API ---
@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'hikes': reverse('hike-list', request=request, format=format),
        'trip-details': reverse('trip-details', request=request, format=format)
    })

class HikeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Hikes to be viewed or edited.
    """
    queryset = Hike.objects.all().order_by('-year')
    serializer_class = HikeSerializer


class TripDetailViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows TripDetails to be viewed or edited.
    """
    queryset = TripDetail.objects.all()
    serializer_class = TripDetailSerializer

# --- testing rest ---
# function based views
@api_view(['GET', 'POST'])
def hike_list_rest(request):
    """
    List all Hikes, or create a new snippet.
    """
    if request.method == 'GET':
        myHikes = Hike.objects.all()
        mySerializer = HikeSerializer(myHikes, many=True)
        return Response(mySerializer.data)

    elif request.method == 'POST':
        mySerializer = HikeSerializer(data = request.data)
        if mySerializer.is_valid():
            mySerializer.save()
            return Response(mySerializer.data, status = status.HTTP_201_CREATED)
        return Response(mySerializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def hike_detail_rest(request, pk):
    """
    Retrieve, update or delete a Hike instance.
    """
    try:
        myHike = Hike.objects.get(pk=pk)
    except Hike.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        mySerializer = HikeSerializer(myHike)
        return Response(mySerializer.data)

    elif request.method == 'PUT':
        mySerializer = HikeSerializer(myHike, data=request.data)
        if mySerializer.is_valid():
            mySerializer.save()
            return Response(mySerializer.data)
        return Response(mySerializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        myHike.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# class based views
class HikeListRest_old(APIView):
    """
    List all Hikes, or create a new Hike.
    """
    def get(self, request, format=None):
        myHikes = Hike.objects.all()
        mySerializer = HikeSerializer(myHikes, many=True)
        return Response(mySerializer.data)

    def post(self, request, format=None):
        mySerializer = HikeSerializer(data = request.data)
        if mySerializer.is_valid():
            mySerializer.save()
            return Response(mySerializer.data, status = status.HTTP_201_CREATED)
        return Response(mySerializer.errors, status=status.HTTP_400_BAD_REQUEST)

class HikeDetailRest_old(APIView):
    """
    Retrieve, update or delete a hike instance.
    """

    def get_object(self, pk):
        try:
            return Hike.objects.get(pk=pk)
        except Hike.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        myHike = self.get_object(pk)
        mySerializer = HikeSerializer(myHike)
        return Response(mySerializer.data)

    def put(self, request, pk, format=None):
        myHike = self.get_object(pk)
        mySerializer = HikeSerializer(myHike, data=request.data)
        if mySerializer.is_valid():
            mySerializer.save()
            return Response(mySerializer.data)
        return Response(mySerializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        myHike = self.get_object(pk)
        myHike.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class HikeListRest(generics.ListCreateAPIView):
    """
    List all Hikes, or create a new Hike.
    """
    queryset = Hike.objects.all()
    serializer_class = HikeSerializer

class HikeDetailRest(generics.RetrieveUpdateDestroyAPIView):
    """
    List all TripDetails, or create a new TripDetail
    """
    queryset = Hike.objects.all()
    serializer_class = HikeSerializer

class TripDetailsListRest(generics.ListCreateAPIView):
    """
    List all Hikes, or create a new Hike.
    """
    queryset = TripDetail.objects.all()
    serializer_class = TripDetailSerializer



# --- HTML API ---

class IndexView(generic.ListView):
    template_name = 'hiking/index.html'

    # by default this returns the list in an object called object_list, so use 'object_list' in the html page.
    # but if 'context_object_name' is defined, then this returned list is named and can be accessed that way in html.
    context_object_name = 'my_hikes_all'

    def get_queryset_old(self):
        #return Hike.objects.all()
        # sort on year descending
        return Hike.objects.order_by('-year')

    def get_queryset(self):
        hike_list = Hike.objects.all().order_by('-year')
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


class DetailsView(generic.DetailView):
    model = Hike
    # by default this would be 'hike_detail.html', but 'template_name' overrides the default name.
    template_name = 'hiking/details.html'
    serializer_class = TripDetailSerializer

#inherits from standard CreateView class that stores form information into the model and to the database
class CreateHike(CreateView):
    model = Hike
    fields = ['title','place','country','date','year','duration','hike_image']

class UpdateHike(UpdateView):
    model = Hike
    fields = ['title','place','country','date','year','duration','hike_image']

class DeleteHike(DeleteView):
    model = Hike
    success_url = reverse_lazy('hiking:index')

class CreateTripDetail(CreateView):
    model = TripDetail
    template_name = 'hiking/create_tripdetail_form.html'
    fields = ['hike','title','description','kind','url','order']
    success_url = reverse_lazy('hiking:index')

class EditTripDetail(UpdateView):
    model = TripDetail
    template_name = 'hiking/edit_tripdetail_form.html'
    fields = ['hike', 'title', 'description', 'kind', 'url','order']
    success_url = reverse_lazy('hiking:index')

class DeleteTripDetail(DeleteView):
    model = TripDetail
    success_url = reverse_lazy('hiking:index')

class myLoginFormView(View):
    form_class = myLoginForm
    template_name = 'hiking/login_form.html'

    # display blank form
    def get(self,request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    # process form data, add user to database
    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            user = form.save(commit=False)

            # cleaned (normalized) data
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            # create a hashed user password
            #user.set_password(password)
            #user.save()

            #returns user object if credentials are correct
            user = authenticate(username=username, password = password)

            if user is not None:

                if user.is_active:
                    login(request,user)
                    return redirect('hiking:index')

        return render(request, self.template_name, {'form': form})


class myRegisterFormView(View):
    form_class = myRegisterForm
    template_name = 'hiking/registration_form.html'

    # display blank form
    def get(self,request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    # process form data, add user to database
    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            user = form.save(commit=False)

            # cleaned (normalized) data
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            # create a hashed user password
            user.set_password(password)
            user.save()

            #returns user object if credentials are correct
            user = authenticate(username=username, password = password)

            if user is not None:

                if user.is_active:
                    login(request,user)
                    return redirect('hiking:index')

        return render(request, self.template_name, {'form': form})

class myContactView(FormView):
    template_name = 'hiking/contact_form.html'
    form_class = myContactForm
    success_url = reverse_lazy('hiking:index')

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        form.send_email()
        return super(myContactView, self).form_valid(form)


"""
Temporary View to test how reacts works on the rest interface.
Call this url in the browser: http://localhost:8000/hiking/react
"""
class ReactView(generic.ListView):
    template_name = 'hiking/my_react.html'

    # by default this returns the list in an object called object_list, so use 'object_list' in the html page.
    # but if 'context_object_name' is defined, then this returned list is named and can be accessed that way in html.
    context_object_name = 'my_hikes_all'

    def get_queryset(self):
        #return Hike.objects.all()
        # sort on year descending
        return Hike.objects.order_by('-year')

    def get_queryset_new(self):
        hike_list = Hike.objects.all().order_by('-year')
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

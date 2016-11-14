from django.shortcuts import render, get_object_or_404

from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from django.views import generic
from django.views.generic import View
from .models import Hike, TripDetail
from .forms import myLoginForm,myRegisterForm, myContactForm

# constants, read from a config later
HIKES_PER_PAGE = 6

class IndexView_old(generic.ListView):
    template_name = 'hiking/index.html'

    # by default this returns the list in an object called object_list, so use 'object_list' in the html page.
    # but if 'context_object_name' is defined, then this returned list is named and can be accessed that way in html.
    context_object_name = 'my_hikes_all'

    def get_queryset(self):
        #return Hike.objects.all()
        # sort on year descending
        return Hike.objects.order_by('-year')

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
        hike_list = Hike.objects.order_by('-year')
        paginator = Paginator(hike_list, HIKES_PER_PAGE)  # Show 25 contacts per page

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
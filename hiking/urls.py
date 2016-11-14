from django.conf.urls import url
from . import views

app_name = 'hiking'

urlpatterns = [
    # /hiking/
    url(r'^$', views.IndexView.as_view(), name='index'),

    # /register/
    url(r'^register/$',views.myRegisterFormView.as_view(), name='register'),

    # /login/
    url(r'^login/$', views.myLoginFormView.as_view(), name='login'),

    # /contact/
    url(r'^contact/$', views.myContactView.as_view(), name='contact'),

    # /hiking/<hike_id>/
    #the regular expression takes the typed in id and stores it in my variable, hike_id
    url(r'^(?P<pk>[0-9]+)/$', views.DetailsView.as_view(), name='details'),

    #/hiking/hike/add/
    url(r'hike/add/$',views.CreateHike.as_view(), name='hike-add'),

    # /hiking/hike/<hike_id>/
    # for now, adding this url to a submit
    url(r'hike/(?P<pk>[0-9]+)/$', views.UpdateHike.as_view(), name='hike-update'),

    # /hiking/hike/<hike_id>/delete
    url(r'hike/(?P<pk>[0-9]+)/delete/$', views.DeleteHike.as_view(), name='hike-delete'),

    # /hiking/hike/<hike_id>/create_TripDetail
    url(r'hike/(?P<pk>[0-9]+)/create_tripdetail/$', views.CreateTripDetail.as_view(), name='detail-create'),

    # /hiking/hike/<hike_id>/edit_TripDetail/<TripDetail_id>
    url(r'edit_tripdetail/(?P<pk>[0-9]+)/$', views.EditTripDetail.as_view(), name='detail-edit'),

    # /hiking/hike/<hike_id>/delete_TripDetail
    url(r'delete_tripdetail/(?P<pk>[0-9]+)/$', views.DeleteTripDetail.as_view(), name='detail-delete'),

]

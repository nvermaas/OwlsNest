from django.conf.urls import url, include
from django.contrib.auth.models import User

from . import views
from rest_framework import routers

app_name = 'hiking'


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.

urlpatterns = [
    # === REST VIEWS ===
    #url(r'^$', views.api_root), # this would short cut the index url
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    # /hiking/rest
    url(r'^rest/$', views.HikeListRest.as_view(), name='hike-list-rest'),

    url(r'^(?P<pk>[0-9]+)/rest$', views.HikeDetailRest.as_view(), name='hike-details-rest'),
    url(r'^(?P<pk>[0-9]+)/rest2', views.TripDetailsListRest.as_view(), name='tripreport-details-rest'),

    # /hiking/<hike_id>/tripdetails

    url(r'tripdetails/(?P<pk>[0-9]+)/$', views.TripDetailsLDetailView.as_view(), name='tripdetails-detail-view'),
    url(r'^(?P<pk>[0-9]+)/tripdetails', views.TripDetailsListView.as_view(), name='tripdetails-list-view'),
    url(r'^tripdetails/$', views.TripDetailsListViewAll.as_view(), name='tripdetails-list-view-all'),

    #------------------------------------------------------------------------------------------

    # /hiking/react (temporary url to test react without the need to start a separate webserver
    url(r'^react$', views.ReactView.as_view(), name='react'),

    # === LOCAL VIEWS ===
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

    # /search/ (triggered by 'action' property of search_box in base.html)
    url(r'^search/$', views.hike_search, name='hike_search'),
    # url(r'^results/$', views.hike_results, name='hike_results'),
    # /query/
    url(r'^query', views.QueryView.as_view(), name='hike_query'),
    url(r'^(?P<pk>[0-9]+)/query/$', views.QueryView.as_view(), name='hike_query')
]

from django.conf.urls import url, include
from django.contrib.auth.models import User

from . import views
from rest_framework import routers

app_name = 'hiking'


# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'hiking', views.HikeViewSet)


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.

urlpatterns = [
    # REST framework

    # the next url reroutes all calls through the router and REST framework
    url(r'^REST/', include(router.urls)),
    url(r'^rest/$', views.HikeListRest.as_view(), name='hike-list'),
    url(r'^(?P<pk>[0-9]+)/rest$', views.HikeDetailRest.as_view(), name='hike-details'),
    url(r'^(?P<pk>[0-9]+)/rest2', views.TripDetailsListRest.as_view()),

    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

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

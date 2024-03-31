
from django.urls import include, path

from . import views

app_name = 'hiking'

urlpatterns = [
    # === REST API VIEWS ===
    # /my_hiking/hike-list-api/
    path('hike-list-api/', views.HikeListAPI.as_view(), name='hike-list-api'),
    path('hike-details-api//<int:pk>/', views.HikeDetailsAPI.as_view(), name='hike-details-api'),

    path('tripdetails-list-api/', views.TripDetailsListAPI.as_view(), name='tripdetails-list-api'),
    path('tripdetails-details-api/<int:pk>/', views.TripDetailsDetailsAPI.as_view(), name='tripdetails-details-api'),

    #------------------------------------------------------------------------------------------

    # === GUI ===
    # /hiking_nico/
    path('', views.IndexView.as_view(), name='index'),

    # /hiking_nico/<hike_id>/
    path('hike/<int:pk>/', views.DetailsView.as_view(), name='details'),

    path('hike/set_filter/<filter>', views.HikeSetFilter, name='hike-set-filter'),
]


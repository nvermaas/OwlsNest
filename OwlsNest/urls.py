from django.contrib import admin
from django.urls import path,include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('hiking_nico/api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('hiking_nico/admin/', admin.site.urls),
    path('hiking_nico/', include('hiking.urls')),
    #path('my_hiking/api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    #path('my_hiking/admin/', admin.site.urls),
    #path('my_hiking/', include('hiking.urls')),
]

# in debug mode the url where media is stored points at a local directory in the project
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import *

urlpatterns = [
	path('image_upload', surface_image_view, name='image_upload'),
    path('prediction',Prediction,name="prediction"),
	path('',Welcome,name='welcome'),
]

if settings.DEBUG:
	urlpatterns += static(settings.MEDIA_URL,
						document_root=settings.MEDIA_ROOT)

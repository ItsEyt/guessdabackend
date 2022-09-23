from django.urls import path
from . import views

urlpatterns = [
        path('', views.index),
        path('getfolder/<int:id>',views.getFolder),
        path('getimage/<int:id>',views.getImage),
]

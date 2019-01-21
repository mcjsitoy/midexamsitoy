from django.urls import path
from . import views
from votes import views


app_name = 'votes'
urlpatterns = [

    path('', views.index, name='index'),
    path('addcandidate/',views.addcandidate, name ='addcandidate'),




]

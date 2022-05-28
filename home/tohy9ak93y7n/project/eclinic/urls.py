from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('modules', views.modules, name='modules'),
    path('modules/search_patient', views.search_patient, name='search_patient'),
    path('modules/clinic', views.clinic, name='clinic'),
]


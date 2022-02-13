from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('modules', views.modules, name='modules'),
    path('modules/registeration', views.registeration, name='registeration'),
    path('modules/clinic', views.clinic, name='clinic'),
]


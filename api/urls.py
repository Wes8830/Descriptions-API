from django.urls import path, re_path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('', views.columns),
    path('columns/', views.columns),
    re_path(r'^(?:column/id=(?P<id>[0-9]+))$', views.columnItem),
    path('bulk/', views.bulkAdd),
]

urlpatterns = format_suffix_patterns(urlpatterns)
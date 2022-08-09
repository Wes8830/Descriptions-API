from django.urls import path, re_path, include
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('', views.home),
    path('users/', views.UserList.as_view(), name='user-list'),
    path('users/<int:pk>/', views.UserDetail.as_view(), name='user-detail'),
    path('columns/', views.ColumnList.as_view(), name='column-list'),
    path('column/<int:pk>', views.ColumnItem.as_view(), name='columns-detail'),
    path('column/<int:pk>', views.ColumnHighlight.as_view(), name='column-highlight'),
]

urlpatterns += [
    path('api-auth/', include('rest_framework.urls'))
]

urlpatterns = format_suffix_patterns(urlpatterns)
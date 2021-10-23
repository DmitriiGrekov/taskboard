from django.urls import path, include
from .views import TaskListUser 


urlpatterns = [
    path('api/v1/list/tasks/', TaskListUser.as_view(), name='taks_list_user'),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken'))
]
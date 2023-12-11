from django.urls import path
from .views import user_info_view,list_users

urlpatterns = [
    path('user_info/create/', user_info_view.as_view(), name='create-yourmodel'),
    path('user-info/list/', list_users.as_view(), name='list-yourmodel'),
]

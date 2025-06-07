from django.urls import path
from . import views
from .views import get_items, CustomAuthToken

urlpatterns = [
    path('items/',get_items,name="get_items"),
    path('items/<int:pk>/',views.item_detail,name="item_details"),
    path('api/login/',CustomAuthToken.as_view(), name='api_login'),
]
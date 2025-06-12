from django.urls import path, include
from . import views
from .views import get_items, CustomAuthToken, ItemDetailsView, ItemViewSet
from rest_framework.routers import DefaultRouter

router=DefaultRouter()
router.register(r'items',ItemViewSet, basename='item')


urlpatterns = [
    # path('items/',get_items,name="get_items"),
    # path('items/<int:pk>/', ItemDetailsView.as_view() ,name="item_details"),
    # path('api/login/',CustomAuthToken.as_view(), name='api_login'),
    path('api/',include(router.urls)),
]
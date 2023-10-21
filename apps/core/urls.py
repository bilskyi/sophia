from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register('group', GroupViewSet)
router.register('course', CourseViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('get-users-by-group/<int:pk>/', GetUsersByGroupViewSet.as_view({'get': 'list'}))

]
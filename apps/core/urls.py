from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *
# router = DefaultRouter()
# router.register(r'students')

urlpatterns = [
    path('', GetCourses.as_view())
    # path('', include(router.urls))
]
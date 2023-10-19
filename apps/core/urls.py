from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register('group', GroupViewSet)

urlpatterns = [
    path('', GetCoursesView.as_view()),
    path('', include(router.urls)),
    path('create/', CreateCourseView.as_view()),
]
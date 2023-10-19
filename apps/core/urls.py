from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *
# router = DefaultRouter()
# router.register(r'students')

urlpatterns = [
    path('', GetCoursesView.as_view()),
    path('create/', CreateCourseView.as_view())
]
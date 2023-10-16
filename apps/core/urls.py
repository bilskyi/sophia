from django.urls import path, include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'students')

urlpatterns = [
    path('', include(router.urls))
]
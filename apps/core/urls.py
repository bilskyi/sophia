from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register('group', GroupViewSet)
router.register('course', CourseViewSet)
router.register('user', UserViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('join/', JoinUserToGroupView.as_view()),
    path('get-users-by-group/<int:pk>/', GetUsersByGroupViewSet.as_view({'get': 'list'})),
    path('delete-user-from-group/<int:group_pk>/<int:user_pk>/', DeleteUserFromGroupView.as_view())
]
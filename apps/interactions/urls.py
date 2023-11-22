from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register('task', CourseTaskViewSet, 'task')

urlpatterns = [
    path('join/', JoinUserToGroupView.as_view()),
    path('delete-user-from-group/<int:group_pk>/<int:user_pk>/', DeleteUserFromGroupView.as_view())
]
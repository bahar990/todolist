from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import Todolistview

router = DefaultRouter()
router.register(r'todolist', Todolistview)

urlpatterns = [
    path('', include(router.urls)),
]

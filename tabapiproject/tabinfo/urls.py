from django.urls import path, include
from rest_framework.routers import DefaultRouter
from tabinfo import views

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'tabinfo', views.TabinfoViewSet)


# The API URLs are now determined automatically by the router.
urlpatterns = [
    path(r'', include(router.urls)),
]

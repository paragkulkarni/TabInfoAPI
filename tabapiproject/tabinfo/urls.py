from django.urls import path, include
from rest_framework.routers import DefaultRouter
from tabinfo import views
from django.conf.urls import url,include
# Create a router and register our viewsets with it.
router = DefaultRouter()
#router.register(r'tabinfo', views.TabinfoViewSet.as_view(),base_name='tabinfo')


# The API URLs are now determined automatically by the router.
urlpatterns = [
    url(r'^users/$', views.TabinfoViewSet.as_view()),
    url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view()),
    url(r'^', include(router.urls)),
]

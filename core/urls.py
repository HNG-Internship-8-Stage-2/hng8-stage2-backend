from django.urls import path, include
from .views import ContactViewSet


POST_OPTIONS = {'post': 'create'}


urlpatterns = [
    path('', ContactViewSet.as_view(POST_OPTIONS), name="data"),
]

from django.conf.urls import url
from qa.views import *


urlpatterns = (
    url(r'^$', test),
)

from django.conf.urls import url
from qa.views import *


urlpatterns = (
    url(r'^$', home_page),
    url(r'^login/', test),
    url(r'^signup/', test),
    url(r'^question/(?P<id>\d+)/', question_page),
    url(r'^ask/', test),
    url(r'^popular/', popular_page),
    url(r'^new/', test),
)

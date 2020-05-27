from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^getdata/$', DataView.as_view(), name='get_data'),

]
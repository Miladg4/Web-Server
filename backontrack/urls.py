# -*- coding: utf-8 -*-

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^export_data', views.export_data),
    url(r'^export_for_chart', views.export_for_chart),
    url(r'^get_schedule', views.get_schedule),
    url(r'^course_charts', views.course_charts),
    url(r'', views.index),
]
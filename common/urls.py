from django.urls import path

from common.views import home_page_view, _404_page_view, success_page_view

app_name = 'common'

urlpatterns = [
    path('', home_page_view, name='home'),
    path('not_found/', _404_page_view, name='404'),
    path('success/', success_page_view, name='success'),
]

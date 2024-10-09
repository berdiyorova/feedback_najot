from django.urls import path

from feedback.views import comment_view, offer_view, offer_form_view

app_name = 'feedback'

urlpatterns = [
    path('comment/', comment_view, name='comment'),
    path('offer/', offer_view, name='offer'),
    path('offer-form/', offer_form_view, name='offer_form'),
]

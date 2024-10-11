from django.urls import path

from feedback.views import comments_view, offers_view, send_offer_view, send_problem_view

app_name = 'feedback'

urlpatterns = [
    path('comments/', comments_view, name='comments'),
    path('offers/', offers_view, name='offers'),
    path('send_offer/', send_offer_view, name='send_offer'),
    path('send_problem/', send_problem_view, name='send_problem'),
]

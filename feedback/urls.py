from django.urls import path

from feedback.views import offers_view, send_offer_view, send_problem_view, offer_or_problem_detail_view

app_name = 'feedback'

urlpatterns = [
    path('offers/', offers_view, name='offers'),
    path('send_offer/', send_offer_view, name='send_offer'),
    path('send_problem/', send_problem_view, name='send_problem'),
    path('<int:pk>/', offer_or_problem_detail_view, name='detail'),
]

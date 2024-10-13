from django.shortcuts import render

from feedback.models import QuestionModel, OfferModel
from teams.models import EmployeeModel


def home_page_view(request):
    questions = QuestionModel.objects.all()
    team = EmployeeModel.objects.all()
    best_offers = OfferModel.objects.filter(status=True)
    context = {
        'questions': questions,
        'team': team,
        'best_offers': best_offers
    }
    return render(request, 'index.html', context)

def _404_page_view(request):
    return render(request, '404.html')

def success_page_view(request):
    return render(request, 'success/success.html')

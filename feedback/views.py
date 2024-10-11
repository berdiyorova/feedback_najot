from django.contrib import messages
from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from feedback.forms import ProblemForm, OfferForm
from feedback.models import ProblemModel, OfferModel


def comments_view(request):
    return render(request, 'comments/comment.html')

def send_problem_view(request):
    if request.method == 'POST':
        form = ProblemForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['problem_title']
            description = form.cleaned_data['problem_description']
            ProblemModel.objects.create(title=title, description=description)
            messages.success(request, 'Your complaint has been successfully submitted!')
            return redirect(reverse_lazy('common:success'))
        else:
            messages.error(request, 'Invalid data.')
    else:
        form = ProblemForm()
    return render(request, 'forms/offer/offer-form.html', {'form': form})

def send_offer_view(request):
    if request.method == 'POST':
        form = OfferForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['offer_title']
            description = form.cleaned_data['offer_description']
            user = request.user
            OfferModel.objects.create(title=title, description=description, user=user)
            messages.success(request, 'Your offer has been successfully submitted!')
            return redirect(reverse_lazy('common:success'))
        else:
            messages.error(request, 'Invalid data.')
    else:
        form = ProblemForm()
    return render(request, 'forms/offer/offer-form.html', {'form': form})

def offers_view(request):
    offers = OfferModel.objects.all()
    problems = ProblemModel.objects.all()
    my_offers = OfferModel.objects.filter(user=request.user)
    context = {
        'offers': offers,
        'problems': problems,
        'my_offers': my_offers
    }
    return render(request, 'offers/offer.html', context)

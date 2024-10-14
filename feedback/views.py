from django.contrib import messages
from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy

from feedback.forms import ProblemForm, OfferForm, CommentForm
from feedback.models import ProblemModel, OfferModel, CommentsModel, LikeOffer, LikeProblem


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
    my_offers = []
    if request.user.is_authenticated:
        my_offers = OfferModel.objects.filter(user=request.user)

    search_query = request.GET.get('q', '')
    if search_query:
        offers = OfferModel.objects.filter(Q(title__icontains=search_query) | Q(description__icontains=search_query))
        problems = ProblemModel.objects.filter(Q(title__icontains=search_query) | Q(description__icontains=search_query))

    context = {
        'offers': offers,
        'problems': problems,
    }
    if my_offers:
        context['my_offers'] = my_offers

    return render(request, 'offers/offer.html', context)


def offer_or_problem_detail_view(request, pk):
    offer = OfferModel.objects.filter(id=pk).first()

    if offer is None:
        offer = ProblemModel.objects.filter(id=pk).first()

    if request.method == 'POST':
        form = CommentForm(data=request.POST)
        if form.is_valid():
            text = form.cleaned_data['text']
            CommentsModel.objects.create(text=text, user=request.user, offer=offer)
            offer.reply_count += 1
            offer.save()
        return render(request, 'comments/comment.html')

    else:
        form = CommentForm()
        context = {
            'offer': offer,
            'form': form
        }
        offer.views_count += 1
        offer.save()
        return render(request, 'comments/comment.html', context)


def like_view(request, pk):
    offer = OfferModel.objects.filter(id=pk).first()

    if offer is not None:
        # Add a like or increment like count
        LikeOffer.objects.get_or_create(user=request.user, offer=offer)
        # Increment the likes count on the post
        offer.likes_count += 1
        offer.save()
    else:
        problem = ProblemModel.objects.filter(id=pk).first()
        # Add a like or increment like count
        LikeProblem.objects.get_or_create(user=request.user, problem=problem)

        # Increment the likes count on the post
        problem.likes_count += 1
        problem.save()

    return render(request, 'comments/comment.html')

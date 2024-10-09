from django.shortcuts import render

def comment_view(request):
    return render(request, 'comments/comment.html')

def offer_form_view(request):
    return render(request, 'forms/offer/offer-form.html')

def offer_view(request):
    return render(request, 'offers/offer.html')

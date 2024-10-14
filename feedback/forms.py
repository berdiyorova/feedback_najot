from django import forms

class ProblemForm(forms.Form):
    problem_title = forms.CharField(max_length=255)
    problem_description = forms.CharField(widget=forms.Textarea)

class OfferForm(forms.Form):
    offer_title = forms.CharField(max_length=255)
    offer_description = forms.CharField(widget=forms.Textarea)

class CommentForm(forms.Form):
    text = forms.CharField(max_length=255)

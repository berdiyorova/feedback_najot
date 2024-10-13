from modeltranslation.translator import TranslationOptions, register
from feedback.models import OfferModel, ProblemModel, QuestionModel

@register(OfferModel)
class OfferTranslationOptions(TranslationOptions):
    fields = ('title', 'description')

@register(ProblemModel)
class ProblemTranslationOptions(TranslationOptions):
    fields = ('title', 'description')

@register(QuestionModel)
class QuestionTranslationOptions(TranslationOptions):
    fields = ('question', 'answer')

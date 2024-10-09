from modeltranslation.translator import translator, TranslationOptions, register
from feedback.models import CommentsModel, OfferModel, ProblemModel

@register(CommentsModel)
class CommentTranslationOptions(TranslationOptions):
    fields = ('text',)

@register(OfferModel)
class OfferTranslationOptions(TranslationOptions):
    fields = ('title', 'description')

@register(ProblemModel)
class ProblemTranslationOptions(TranslationOptions):
    fields = ('title', 'description')

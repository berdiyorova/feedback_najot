from modeltranslation.translator import translator, TranslationOptions, register
from feedback.models import CommentsModel, OfferModel, ProblemModel

@register(CommentsModel)
class CommentTranslationOptions(TranslationOptions):
    fields = ('text', 'likes_count', 'views_count', 'reply_count', 'user')

@register(OfferModel)
class OfferTranslationOptions(TranslationOptions):
    fields = ('title', 'description', 'user')

@register(ProblemModel)
class ProblemTranslationOptions(TranslationOptions):
    fields = ('title', 'description')

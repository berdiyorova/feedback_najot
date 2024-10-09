from modeltranslation.translator import translator, TranslationOptions, register
from users.models import CustomUserModel

@register(CustomUserModel)
class CustomUserTranslationOptions(TranslationOptions):
    fields = ('username', 'first_name', 'last_name')

from modeltranslation.translator import TranslationOptions, register
from teams.models import EmployeeModel

@register(EmployeeModel)
class EmployeeTranslationOptions(TranslationOptions):
    fields = ('position', 'bio')

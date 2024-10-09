from modeltranslation.translator import translator, TranslationOptions, register
from teams.models import EmployeeModel

@register(EmployeeModel)
class EmployeeTranslationOptions(TranslationOptions):
    fields = ('position',)

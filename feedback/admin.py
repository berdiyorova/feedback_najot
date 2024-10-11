from django.contrib import admin

from feedback.models import CommentsModel, OfferModel, ProblemModel, QuestionModel


admin.site.register(CommentsModel)
admin.site.register(OfferModel)
admin.site.register(ProblemModel)
admin.site.register(QuestionModel)

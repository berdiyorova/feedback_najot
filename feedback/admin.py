from django.contrib import admin

from feedback.models import CommentsModel, OfferModel, ProblemModel

admin.site.register(CommentsModel)
admin.site.register(OfferModel)
admin.site.register(ProblemModel)

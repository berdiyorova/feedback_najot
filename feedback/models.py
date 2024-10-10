from django.db import models
from django.utils.translation import gettext_lazy as _

from common.models import AbstractBaseModel
from users.models import CustomUserModel

class CommentsModel(AbstractBaseModel):
    text = models.TextField(verbose_name=_("Comment text"))
    likes_count = 0
    views_count = 0
    reply_count = 0
    user = models.ForeignKey(
        CustomUserModel,
        on_delete=models.SET_NULL,
        null=True,
        related_name='comments',
        verbose_name=_('Comment user')
    )

    class Meta:
        verbose_name = _('Comment')
        verbose_name_plural = _('Comments')


class ProblemModel(AbstractBaseModel):
    title = models.CharField(max_length=255, verbose_name=_('Title'))
    description = models.TextField(verbose_name=_("Description"))

    class Meta:
        verbose_name = _('Problem')
        verbose_name_plural = _('Problems')


class OfferModel(AbstractBaseModel):
    title = models.CharField(max_length=255, verbose_name=_('Title'))
    description = models.TextField(verbose_name=_("Description"))
    status = models.BooleanField(default=False)
    user = models.ForeignKey(
        CustomUserModel,
        on_delete=models.SET_NULL,
        null=True,
        related_name='offers',
        verbose_name=_("User")
    )

    class Meta:
        verbose_name = _('Offer')
        verbose_name_plural = _('Offers')


class QuestionModel(AbstractBaseModel):
    q_title = models.CharField(max_length=255, verbose_name=_("Question title"))
    question = models.TextField(verbose_name=_("Question text"))
    answer = models.TextField(verbose_name=_("Answer"))

    def __str__(self):
        return self.q_title

    class Meta:
        verbose_name = "Question"
        verbose_name_plural = "Questions"

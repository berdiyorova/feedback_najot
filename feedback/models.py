from django.db import models
from django.utils.translation import gettext_lazy as _

from common.models import AbstractBaseModel
from users.models import CustomUserModel


class ProblemModel(AbstractBaseModel):
    title = models.CharField(max_length=255, verbose_name=_('Title'))
    description = models.TextField(verbose_name=_("Description"))
    likes_count = models.PositiveSmallIntegerField(default=0)
    views_count = models.PositiveSmallIntegerField(default=0)
    reply_count = models.PositiveSmallIntegerField(default=0)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Problem')
        verbose_name_plural = _('Problems')


class OfferModel(AbstractBaseModel):
    title = models.CharField(max_length=255, verbose_name=_('Title'))
    description = models.TextField(verbose_name=_("Description"))
    status = models.BooleanField(default=False)
    likes_count = models.PositiveSmallIntegerField(default=0)
    views_count = models.PositiveSmallIntegerField(default=0)
    reply_count = models.PositiveSmallIntegerField(default=0)
    user = models.ForeignKey(
        CustomUserModel,
        on_delete=models.SET_NULL,
        null=True,
        related_name='offers',
        verbose_name=_("User")
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Offer')
        verbose_name_plural = _('Offers')


class CommentsModel(AbstractBaseModel):
    text = models.TextField(verbose_name=_("Comment text"))
    user = models.ForeignKey(
        CustomUserModel,
        on_delete=models.SET_NULL,
        null=True,
        related_name='comments',
        verbose_name=_('Comment user')
    )
    offer = models.ForeignKey(OfferModel, related_name=_("Comments"), on_delete=models.CASCADE, null=True, blank=True)
    problem = models.ForeignKey(ProblemModel, related_name=_("Comments"), on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = _('Comment')
        verbose_name_plural = _('Comments')


class QuestionModel(AbstractBaseModel):
    question = models.TextField(verbose_name=_("Question text"))
    answer = models.TextField(verbose_name=_("Answer"))

    def __str__(self):
        return self.question

    class Meta:
        verbose_name = "Question"
        verbose_name_plural = "Questions"

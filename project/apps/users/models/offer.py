from django.contrib.auth import get_user_model
from django.db import models
from sorl.thumbnail import ImageField
from apps.commons.models import ImageModel
from apps.commons.storage import HashedImageStorage
from django.core.validators import MaxValueValidator, MinValueValidator


class Offer(models.Model):
    '''Model of offers/gigs'''
    
    user = models.ForeignKey(
        get_user_model(),
        verbose_name='Пользователь',
        on_delete=models.CASCADE,
        related_name='offers'
    )
    title = models.CharField('Краткое описание', max_length=200)
    description = models.TextField('Описание предложения', blank=True, null=True)
    users_liked = models.ManyToManyField(
        get_user_model(),
        verbose_name='Пользователи, которые отметили оффер "Мне нравится"',
        related_name='offer_likes',
        blank=True
    )
    tags = models.ManyToManyField(
        'tags.Tag',
        related_name='offer_tags',
    )
    # TODO: подумать
    number_of_offers_done = models.PositiveIntegerField(
        'Количество выполнений оффера',
        default=0
    )


    def __str__(self):
        return self.title

    @property
    def total_likes(self):
        return self.users_liked.count()
    

    class Meta:
        verbose_name = 'Оффер'
        verbose_name_plural = 'Офферы'

    
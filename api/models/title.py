from django.db import models

from .category import Category
from .genre import Genre
from .utils import year_validator


class Title(models.Model):
    name = models.CharField(
        max_length=300,
        verbose_name='name',
        help_text='Укажите название произведения',
        blank=False
    )
    category = models.ForeignKey(
        Category,
        verbose_name='Категория',
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name='titles',
    )
    genre = models.ManyToManyField(
        Genre,
        verbose_name='Жанр',
        blank=True,
        null=True,
        related_name='titles',
    )
    year = models.PositiveSmallIntegerField(
        verbose_name='Год выпуска',
        default=2021,
        validators=[year_validator],
        db_index=True
    )
    description = models.CharField(
        max_length=1000,
        verbose_name='Описание',
        blank=True,
    )

    class Meta:
        verbose_name = 'Произведение'
        verbose_name_plural = 'Произведения'

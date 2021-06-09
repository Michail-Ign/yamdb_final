from django.db import models


class Genre(models.Model):
    name = models.CharField(
        verbose_name='Жанр',
        max_length=32,
        help_text='Укажите жанр',
    )
    slug = models.SlugField(
        verbose_name='slug',
        unique=True,
        db_index=True,
    )

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'
        ordering = ['name']

    def __str__(self):
        return f'Жанр: {self.name}'

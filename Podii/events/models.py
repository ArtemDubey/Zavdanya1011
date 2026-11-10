from django.conf import settings
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name='Назва')

    class Meta:
        verbose_name = 'Категорія'
        verbose_name_plural = 'Категорії'

    def __str__(self):
        return self.name


class Event(models.Model):
    class Status(models.TextChoices):
        DRAFT = 'draft', 'Чернетка'
        PUBLISHED = 'published', 'Опублікований'
        CANCELLED = 'cancelled', 'Скасований'
        COMPLETED = 'completed', 'Завершений'

    title = models.CharField(max_length=255, verbose_name='Назва заходу')
    description = models.TextField(verbose_name='Опис')
    category = models.ForeignKey(
        Category,
        on_delete=models.PROTECT,
        related_name='events',
        verbose_name='Категорія',
    )
    date = models.DateTimeField(verbose_name='Дата та час проведення')
    price = models.DecimalField(
        max_digits=10, decimal_places=2, default=0, verbose_name='Ціна'
    )
    organizer = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        related_name='organized_events',
        verbose_name='Організатор',
    )
    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.DRAFT,
        verbose_name='Статус',
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['date']
        verbose_name = 'Захід'
        verbose_name_plural = 'Заходи'

    def __str__(self):
        return f'{self.title} ({self.date:%Y-%m-%d %H:%M})'
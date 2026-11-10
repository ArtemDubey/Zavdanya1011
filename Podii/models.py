from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):

  class Role(models.TextChoices):
    USER = 'user', 'User'
    ADMIN = 'admin', 'Admin'
    MODERATOR = 'moderator', 'Moderator'

  role = models.CharField(
      max_length=20, choices=Role.choices, default=Role.USER, verbose_name='Роль'
  )
  groups = models.ManyToManyField(
      'auth.Group',
      verbose_name='groups',
      blank=True,
      related_name='podii_user_set',
      related_query_name='podii_user',
  )
  user_permissions = models.ManyToManyField(
      'auth.Permission',
      verbose_name='user permissions',
      blank=True,
      related_name='podii_user_set_permissions',
      related_query_name='podii_user_permission',
  )

  def __str__(self):
    return f'{self.username} ({self.role})'


class Event(models.Model):

  class Status(models.TextChoices):
    ACTIVE = 'active', 'Активний'
    CANCELLED = 'cancelled', 'Скасований'
    COMPLETED = 'completed', 'Завершений'

  title = models.CharField(max_length=255, verbose_name='Назва заходу')
  description = models.TextField(verbose_name='Опис')
  category = models.CharField(max_length=100, verbose_name='Категорія')
  date = models.DateTimeField(verbose_name='Дата та час проведення')
  price = models.DecimalField(
      max_digits=10, decimal_places=2, verbose_name='Ціна'
  )
  organizer = models.ForeignKey(
      User,
      on_delete=models.CASCADE,
      related_name='organized_events',
      verbose_name='Організатор',
  )
  status = models.CharField(
      max_length=20,
      choices=Status.choices,
      default=Status.ACTIVE,
      verbose_name='Статус',
  )
  views_count = models.PositiveIntegerField(
      default=0, verbose_name='популярність'
  )
  created_at = models.DateTimeField(
      auto_now_add=True, verbose_name='Дата створення'
  )

  def __str__(self):
    return f'{self.title} ({self.date.strftime("%Y-%m-%d %H:%M")})'


class Booking(models.Model):

  user = models.ForeignKey(
      User,
      on_delete=models.CASCADE,
      related_name='bookings',
      verbose_name='Користувач',
  )
  event = models.ForeignKey(
      Event,
      on_delete=models.CASCADE,
      related_name='bookings',
      verbose_name='Захід',
  )
  created_at = models.DateTimeField(
      auto_now_add=True, verbose_name='Дата бронювання'
  )

  class Meta:
    constraints = [
        models.UniqueConstraint(
            fields=['user', 'event'], name='unique_user_event_booking'
        )
    ]
    verbose_name = 'Бронювання'
    verbose_name_plural = 'Бронювання'

  def __str__(self):
    return f'{self.user.username} -> {self.event.title}'
from django.conf import settings
from django.db import models


class Booking(models.Model):
    class Status(models.TextChoices):
        ACTIVE = 'active', 'Активне'
        CANCELLED = 'cancelled', 'Скасоване'
        COMPLETED = 'completed', 'Завершене'

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='bookings',
        verbose_name='Користувач',
    )
    event = models.ForeignKey(
        'events.Event',
        on_delete=models.CASCADE,
        related_name='bookings',
        verbose_name='Захід',
    )
    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.ACTIVE,
        verbose_name='Статус',
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['user', 'event'],
                name='unique_user_event_booking',
            )
        ]
        verbose_name = 'Бронювання'
        verbose_name_plural = 'Бронювання'

    def __str__(self):
        return f'{self.user.username} -> {self.event.title}'
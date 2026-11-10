from datetime import datetime
from Podii.booking.models import Booking
from Podii.events.models import Event
from Podii.accounts.models import User


def create_booking(user: User, event: Event) -> Booking:
  current_time = datetime.now()
  if event.organizer == user:
    raise ValueError('Організатор не може бронювати власний захід.')
  if event.status == Event.Status.CANCELLED:
    raise ValueError('Неможливо забронювати скасований захід.')
  if event.status == Event.Status.COMPLETED:
    raise ValueError('Цей захід уже завершився.')
  if event.date <= current_time:
    raise ValueError('Цей захід уже розпочався.')
  if Booking.objects.filter(user=user, event=event).exists():
    raise ValueError('Ви вже забронювали цей захід.')

  return Booking.objects.create(user=user, event=event)
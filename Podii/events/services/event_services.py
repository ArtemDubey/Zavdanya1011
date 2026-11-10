from Podii.accounts.models import User
from Podii.events.models import Event


def create_event(organizer: User, data: dict) -> Event:
  if organizer.role not in [User.Role.ADMIN, User.Role.MODERATOR]:
    raise PermissionError('Лише адміністратор або модератор може створювати заходи.')
  return Event.objects.create(organizer=organizer, **data)
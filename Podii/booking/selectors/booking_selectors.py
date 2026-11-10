from Podii.booking.models import Booking


def get_user_bookings(user):
  return Booking.objects.filter(user=user).select_related('event')
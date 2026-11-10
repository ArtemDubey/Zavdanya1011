from django.shortcuts import get_object_or_404, redirect, render
from Podii.booking.selectors.booking_selectors import get_user_bookings
from Podii.booking.services.booking_services import create_booking
from Podii.events.models import Event


def book_event_view(request, event_id):
  event = get_object_or_404(Event, id=event_id)

  if request.method == "POST":
    try:
      create_booking(user=request.user, event=event)
      return redirect("booking_history")
    except ValueError as e:
      error_message = str(e)
      return render(
          request,
          "booking/book_error.html",
          {"error": error_message, "event": event},
      )

  return render(request, "booking/book_confirm.html", {"event": event})
def booking_history_view(request):
  bookings = get_user_bookings(request.user)
  context = {"bookings": bookings}
  return render(request, "booking/history.html", context)
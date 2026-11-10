from Podii.events.models import Event


def get_filtered_events(
    category_id=None, min_price=None, max_price=None, sort_by='date'
):
  events = Event.objects.filter(status=Event.Status.PUBLISHED)

  if category_id:
    events = events.filter(category_id=category_id)
  if min_price is not None:
    events = events.filter(price__gte=min_price)
  if max_price is not None:
    events = events.filter(price__lte=max_price)

  return events.order_by(sort_by)
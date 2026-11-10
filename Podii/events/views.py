from django.shortcuts import render
from Podii.events.selectors.event_selectors import get_filtered_events


def event_list_view(request):
  category_id = request.GET.get("category")
  min_price = request.GET.get("min_price")
  max_price = request.GET.get("max_price")
  sort_by = request.GET.get("sort_by", "date")
  events = get_filtered_events(
      category_id=category_id,
      min_price=min_price,
      max_price=max_price,
      sort_by=sort_by,
  )

  context = {
      "events": events,
  }
  return render(request, "events/event_list.html", context)
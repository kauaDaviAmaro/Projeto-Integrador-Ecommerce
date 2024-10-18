from django.shortcuts import render
from django.http import Http404
from .models import Event

def home(request):
    template = 'events.html'
    events = Event.objects.all()
    
    return render(request, template, {'events': events})

def eventDetail(request):
    template = 'eventDetail.html'
    return render(request, template)

def event_detail(request, event_id):
    try:
        event = Event.objects.get(id=event_id)
        if event is None:
            raise Http404("Event not found")
    except Event.DoesNotExist:
        raise Http404("Event not found")
    except Exception as e:
        raise Http404("Error loading event: " + str(e))
    return render(request, 'eventDetail.html', {'event': event})

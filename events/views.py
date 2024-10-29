from django.shortcuts import render
from django.http import Http404
from .models import Event, Appointment
from django.shortcuts import get_object_or_404
from django.utils import timezone

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


def register(request, event_id):
    event = get_object_or_404(Event, id=event_id)

    def get_available_dates(event, days):
        date_now = timezone.now().date()
        date_available = []

        for i in range(days):
            date = date_now + timezone.timedelta(days=i)
            
            if not Appointment.objects.filter(event=event, date_time__date=date).exists():
                date_available.append(date)

        return date_available
    
    dates_available = get_available_dates(event, 30)

    template = 'event_appointment.html'
    return render(request, template, {
        'event': event,
        'dates_available': dates_available
    })

def register_appointment(request, event_id, date):
    '''
    User information is collected here
    '''

    if request.method == 'POST':
        name = request.POST.get('user_name')
        email = request.POST.get('user_email')
        phone = request.POST.get('user_phone')
        notes = request.POST.get('notes')

        appointment = Appointment(
            event_id=event_id,
            date_time=date,
            user_name=name,
            user_email=email,
            user_phone=phone,
            notes=notes
        )
        appointment.save()

        return render(request, 'appointment_success.html')
    
    template = 'appointment.html'
    return render(request, template)
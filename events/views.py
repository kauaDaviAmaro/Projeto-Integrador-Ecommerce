from django.shortcuts import render
from django.http import Http404
from .models import Event, Appointment
from django.shortcuts import get_object_or_404
from django.utils import timezone
import calendar
from django.http import JsonResponse


def home(request):
    template = 'events.html'
    events = Event.objects.all()
    
    return render(request, template, {'events': events})

def event_detail(request, event_id):
    try:
        event = Event.objects.get(id=event_id)

        event_hours = event.duration.total_seconds() / 3600
        event.hours = round(event_hours)

        event_minutes = (event.duration.total_seconds() / 60) % 60
        if event_minutes != 0:
            event.minutes = round(event_minutes)

        if event is None:
            raise Http404("Event not found")
    except Event.DoesNotExist:
        raise Http404("Event not found")
    except Exception as e:
        raise Http404("Error loading event: " + str(e))
    return render(request, 'eventDetail.html', {'event': event})


def register(request, event_id):
    event = get_object_or_404(Event, id=event_id)

    def get_available_dates(event, days=30):
        """Retorna uma lista de datas disponíveis para agendamento em um evento específico."""
        today = timezone.now().date()
        available_dates = []

        for i in range(days):
            date_to_check = today + timezone.timedelta(days=i)
            
            # Verifica se não há agendamentos para o evento nesta data específica
            if not Appointment.objects.filter(event=event, date_time__date=date_to_check).exists():
                available_dates.append(date_to_check)

        return available_dates
    
    # Calcula as datas disponíveis para os próximos 30 dias
    available_dates = get_available_dates(event)

    # Renderiza o template com o evento e as datas disponíveis
    template = 'event_appointment.html'
    return render(request, template, {
        'event': event,
        'available_dates': available_dates  # Mudança de nome para consistência
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

def get_available_dates(request, event_id, year, month):
    event = get_object_or_404(Event, id=event_id)
    
    _, last_day = calendar.monthrange(year, month)
    start_date = timezone.datetime(year, month, 1).date()
    end_date = timezone.datetime(year, month, last_day).date()
    
    today = timezone.now().date()
    dates_available = []
    for day in range(1, last_day + 1):
        date = timezone.datetime(year, month, day).date()
        if date >= today and not Appointment.objects.filter(event=event, date_time=date).exists():
            dates_available.append(date)
    
    return JsonResponse({"available_dates": [date.strftime("%Y-%m-%d") for date in dates_available]})
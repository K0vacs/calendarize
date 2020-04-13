import datetime
from django.views.generic import ListView
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from bookings.models import Bookings
from staff.models import Staff
from equipment.models import Equipment
from .forms import searchForm

class ScheduleTable(ListView):
    # This class extends the ListView class and displays the schedule data to the user.

    model = Bookings
    template_name = 'schedule.html'
    context_object_name = 'pages'

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        context["title"] = "Schedule"
        context["staff"] = Staff.objects.all().values('username', 'image')
        context['equipment'] = Equipment.objects.values()
        context["form"] = searchForm()

        try: 
            pk_date = self.kwargs["date"]
        except:    
            pk_date = datetime.date.today().strftime("%d-%m-%Y")

        context['date'] = datetime.datetime.strptime(
            pk_date, 
            "%d-%m-%Y"
        ).strftime("%d %B %Y")
        
        return context

    def get_queryset(self):

        try: 
            pk_date =  self.kwargs["date"]
        except:    
            pk_date = datetime.date.today().strftime("%d-%m-%Y")

        db_date = datetime.datetime.strptime(pk_date, "%d-%m-%Y").strftime("%d/%m/%Y")

        return self.model.objects.filter(date=db_date).values_list(
            'id',
            'date',
            'start_time',
            'end_time',
            'service_id__name',
            'equipment_id__name',
            'staff_id__username',
        )

    def post(self, request, *args, **kwargs):
        
        search_date = searchForm(request.POST or None, initial={'date': 'today'})
        
        if search_date.is_valid():
            return self.form_valid(search_date)
        else:
            return self.form_invalid(search_date)

    def form_valid(self, search_date):

        date = datetime.datetime.strptime(
            str(
                search_date.cleaned_data['search_date']
            ), 
            "%Y-%m-%d"
            ).strftime('%d-%m-%Y')

        return HttpResponseRedirect(
            reverse(
                'schedule:schedule_date', 
                kwargs = { 
                    "date": date
                }
            )
        )

    def form_invalid(self, search_date):

        try: 
            pk_date =  self.kwargs["date"]
        except:    
            pk_date = datetime.date.today().strftime("%d-%m-%Y")

        db_date = datetime.datetime.strptime(
            pk_date, 
            "%d-%m-%Y"
        ).strftime("%d/%m/%Y")
        
        context = {
            "date": datetime.datetime.strptime(
                pk_date, 
                "%d-%m-%Y"
            ).strftime("%d %B %Y"),
        }

        return render(self.request, self.template_name, context)
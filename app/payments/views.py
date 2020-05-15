import stripe
from django.conf import settings
from django.views.generic.base import TemplateView
from django.shortcuts import render
from staff.forms import StaffForm
from .forms import ContactForm
from django.core.mail import send_mail



import logging
logger = logging.getLogger(__name__)

stripe.api_key = settings.STRIPE_SECRET_KEY

class HomePageView(TemplateView):
    template_name = 'pay.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['key'] = settings.STRIPE_PUBLISHABLE_KEY
        context['contactForm'] = ContactForm()
        context['staff'] = StaffForm()
        return context

    def post(self, request, *args, **kwargs):
        form = ContactForm(request.POST)

        if form.is_valid():
            send_mail(
                'Calendarize Enquiry',
                form.cleaned_data['message'],
                'Calendarize <info@4kmedia.co.za>',
                [form.cleaned_data['email']],
                fail_silently=False,
            )

            return render(request, self.template_name, {
                'key': settings.STRIPE_PUBLISHABLE_KEY,
                'contactForm': ContactForm(),
                'staff': StaffForm(),
                })




def charge(request):
    if request.method == 'POST':

        charge = stripe.Charge.create(
            amount=500,
            currency='eur',
            description='A Django charge',
            source=request.POST['stripeToken']
        )

        if(charge.paid == True):
            staff = StaffForm(request.POST)

            if staff.is_valid():
                staff.save()
                logger.warning("Save Staff")

                return render(request, 'charge.html')
        else:
            logger.warning("Failed try again page")

        return render(request, 'charge.html')
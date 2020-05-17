import stripe
from django.conf import settings
from django.views.generic.base import TemplateView
from django.shortcuts import render
from staff.forms import StaffForm
from .forms import ContactForm
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.urls import reverse
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

            try:
                
                send_mail(
                    'Calendarize Enquiry',
                    form.cleaned_data['message'],
                    'Calendarize <info@4kmedia.co.za>',
                    [form.cleaned_data['email']],
                    fail_silently=False,
                )

                message = 'success'

            except:

                message = 'failed'
                logger.warning("Contact form submission failed")

            return HttpResponseRedirect(reverse('contact', kwargs = { 'message': message }))


class FormSubmission(TemplateView):
    template_name = 'form-submission.html'


class PaymentSubmission(TemplateView):
    template_name = 'charge.html'

    def post(self, request, *args, **kwargs):

        try:

            charge = stripe.Charge.create(
                amount=500,
                currency='eur',
                description='Calendarize Shared',
                source=request.POST['stripeToken']
            )

            if(charge.paid == True):
                staff = StaffForm(request.POST)

            if staff.is_valid():
                staff.save()

            message = "success"

        except:

            logger.warning("Failed to process payment")
            message = "failed"

        return HttpResponseRedirect(reverse('charge', kwargs = { 'message': message }))
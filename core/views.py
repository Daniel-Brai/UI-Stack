from django.views.generic import TemplateView
from django.shortcuts import render
from .forms import ContactForm, WaitlistForm

# Create your views here.
class LandingPage(TemplateView):
    template_name = 'core/landing.html'

    def get(self, request, *args, **kwargs):
        form1 = ContactForm()
        form2 = WaitlistForm()
        return render(request, self.template_name, { "contact_form": form1, "waitlist_form" : form2 })

    def post(self, request, *args, **kwargs):
        form = ContactForm(request.POST)
        if form.clean_fields():
            return render(request, self.template_name, { "message": "Email sent" })
        return render(request, self.template_name, { "form" : form })


class PrivacyPage(TemplateView):
    template_name = 'core/privacy.html'
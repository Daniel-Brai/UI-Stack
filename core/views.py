from django.views.generic import TemplateView
from django.shortcuts import render
from .forms import ContactForm, WaitlistForm
from .models import WaitlistUser

# Create your views here.
class LandingPage(TemplateView):
    template_name = 'core/landing.html'

    def get(self, request, *args, **kwargs):
        form1 = ContactForm()
        form2 = WaitlistForm()
        return render(request, self.template_name, { "contact_form": form1, "waitlist_form" : form2, "success": "False" })

    def post(self, request, *args, **kwargs):
        new_w_form = WaitlistForm()
        new_c_form = ContactForm()

        if request.POST.get('form_type') == 'contact':
            c_form = ContactForm(request.POST)
            if c_form.is_valid():
                return render(request, self.template_name, { "c_message": "Email sent", "waitlist_form": new_w_form, "contact_form": new_c_form, "success": "True" })
            return render(request, self.template_name, { "waitlist_form" : new_w_form, "contact_form": new_c_form, "success": "False" })

        if request.POST.get('form_type') == 'waitlist':
            w_form = WaitlistForm(request.POST)
            if w_form.is_valid():
                email = w_form.cleaned_data['email']
                user = WaitlistUser.objects.create(email=email)
                user.save()
                return render(request, "includes/waitlist__confirm.html", { "w_message": "Email sent", "waitlist_form": new_w_form, "contact_form": new_c_form, "success": "True" })
            return render(request, self.template_name, { "waitlist_form" : new_w_form, "contact_form": new_c_form, "success": "False" })

class PrivacyPage(TemplateView):
    template_name = 'core/privacy.html'
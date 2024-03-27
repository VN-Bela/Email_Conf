from django.http import HttpResponseRedirect
from django.shortcuts import render,reverse
from django.conf import settings
from django.core.mail import send_mail,EmailMessage

from django.views.generic import TemplateView, FormView
from .forms import ContactForm
# Create your views here.


class SuccessView(TemplateView):
    template_name="success.html"
class IndexView(TemplateView):
    template_name="index.html"

class ContactView(FormView):
    form_class=ContactForm
    template_name="contact.html"
    def form_valid(self, form):
        email = form.cleaned_data.get("email")
        subject = form.cleaned_data.get("subject")
        message = form.cleaned_data.get("message")
        full_message = f"""   
                        Received Message from {email}, Subject: {subject}
                        --------------------------------------------------

                        {message}
                        """
        msg=EmailMessage(
            subject="Received contact form submission",
            body=full_message,
            from_email=settings.EMAIL_HOST_USER,
            to=["bela.vnurture@gmail.com"]
        )
        msg.send()
        print("Done")
        # Redirecting to a success URL
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        # Assuming you have a URL named 'success' in your urls.py
        return reverse('success')  # or return '/success/' if you prefer to hard-code the URL
    
     

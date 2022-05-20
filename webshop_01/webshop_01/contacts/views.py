from django.shortcuts import render, redirect
from django.views.generic import TemplateView

from webshop_01.common.email_sender import contact_email_message
from webshop_01.contacts.forms import ContactForm


class ContactView(TemplateView):
    template_name = 'pages/contact.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        contact_form = ContactForm()
        context['contact_form'] = contact_form
        return context

    def post(self, request):
        form = ContactForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message_content = form.cleaned_data['message_content']
            contact_email_message(first_name, email, subject, message_content)
        # TODO Message On Success Or Error Message!
        return redirect('contact')

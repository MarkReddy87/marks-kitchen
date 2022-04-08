""" relevant imports below """
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views import generic, View
from .models import Contact
from .forms import ContactForm, BookingForm


class ShowMenu(generic.ListView):
    """ ShowMenu view """
    template_name = 'index.html'
    queryset = HttpResponse


class ShowContacts(generic.ListView):
    """ ShowContact view """
    model = Contact
    queryset = Contact.objects.filter(approved=True).order_by('created_on')
    template_name = 'review.html'
    paginate_by = 6


class ReviewDetail(View):
    """ ReviewDetail view """
    def get(self, request, slug, *args, **kwargs):
        """ function to get specific review """
        queryset = Contact.objects.filter(approved=True)
        review = get_object_or_404(queryset, slug=slug)
        return render(
            request,
            "review_detail.html",
            {
                "review": review
            },
        )


class EditContact(generic.ListView):
    """ EditContact view """
    def get(self, request, *args, **kwargs):

        # contact = get_object_or_404(Contact, id=)


        return render(
            request,
            'edit_contact.html',
            {
                "contacted": False,
                "contact_form": ContactForm()
            },
        )

    def post(self, request, id):
        """ Post request function """

        contact_form = ContactForm(data=request.POST)

        if contact_form.is_valid():
            contact_form.save()
        else:
            contact_form = ContactForm()

        return render(
            request,
            'edit_contact.html',
            {
                "contacted": True,
                "contact_form": ContactForm()
            },
        )




class ContactList(generic.ListView):
    """ ContactList view """

    def get(self, request, *args, **kwargs):

        return render(
            request,
            'contact.html',
            {
                "contacted": False,
                "contact_form": ContactForm()
            },
        )

    def post(self, request):
        """ Post request function """

        contact_form = ContactForm(data=request.POST)

        if contact_form.is_valid():
            contact_form.save()
        else:
            contact_form = ContactForm()

        return render(
            request,
            'contact.html',
            {
                "contacted": True,
                "contact_form": ContactForm()
            },
        )


class BookingList(generic.ListView):
    """ BookingList view """

    def get(self, request):

        return render(
            request,
            'booking.html',
            {
                "booked": False,
                "booking_form": BookingForm()
            },
        )

    def post(self, request):
        """ Post request function """

        booking_form = BookingForm(data=request.POST)

        if booking_form.is_valid():
            booking_form.save()
        else:
            booking_form = BookingForm()

        return render(
            request,
            'booking.html',
            {
                "booked": True,
                "booking_form": BookingForm()
            },
        )

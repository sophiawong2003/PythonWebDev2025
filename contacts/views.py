from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from . models import Contact
from django.core.mail import send_mail
# Create your views here.
def contact(request):
    if request.method == 'POST':
        listing_id = request.POST["listing_id"]
        listing = request.POST["listing"]
        name = request.POST["name"]
        email = request.POST["email"]
        phone = request.POST["phone"]
        message = request.POST["message"]
        user_id = request.POST["user_id"]
        realtor_email = request.POST["realtor_email"]
        if request.user.is_authenticated:
            #user_id = request.user.id
            has_contacted = Contact.objects.all().filter(listing_id=listing_id, user_id=user_id)
            if has_contacted:
                messages.error(request, "You have already made an inquiry for this listing")
                return redirect('/listings/'+listing_id)
        contact = Contact(listing=listing, listing_id=listing_id, name=name, email=email, phone=phone, message=message, user_id=user_id)
        contact.save()
        # send email
        send_mail(
            'Property Listing Inquiry',
            'There has been an inquiry for ' + listing + '. Sign into the admin panel for more info',
            'bustyle@pm.me', # from admin email
            [realtor_email], # to email 
            fail_silently=False
        )
        messages.success(request,"Your request has been submitted, a realtor will get back to you soon")    
    return redirect('/listings/'+listing_id)

def delete_contact(request, contact_id):
    contact = get_object_or_404(Contact, pk=contact_id)
    contact.delete()
    return redirect('dashboard')
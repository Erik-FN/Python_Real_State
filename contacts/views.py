from django.shortcuts import render,redirect
from .models import Contact
from django.contrib import messages
from django.core.mail import send_mail

# Create your views here.

def contact(request):
    if request.method == 'POST':
        listing_id = request.POST['listing_id']
        listing = request.POST['listing']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        user_id = request.POST['user_id']
        realtor_email = request.POST['realtor_email']

        #Check if the user made an inquiry for that propery already
        if request.user.is_authenticated:
            user_id = request.user.id
            has_contacted = Contact.objects.all().filter(listing_id = listing_id, user_id = user_id)

            if has_contacted:

                messages.error(request, 'You already have an inquiry for this propery, wait for a response before making a new one')
                return redirect ('/listings/'+listing_id)
            
        contact = Contact(listing=listing, listing_id=listing_id, name=name, email=email, realtor_email=realtor_email,user_id=user_id,message=message, phone=phone)
        contact.save()

        send_mail(
            'Property Lising inquiry',
            'There has been an inquiry for '+listing+' Sign into the admin panel to look at the contact',
            'erikdevportfolio@gmail.com',
            [realtor_email, 'nomadshae@gmail.com'],
            fail_silently=False
        )
        
        messages.success(request, 'Request sumbited')
        
        return redirect('/listings/'+listing_id)

from django.shortcuts import render

from django.http import HttpResponse,HttpResponseRedirect

from django.contrib.auth import authenticate, login,logout
from django.urls import reverse 


from django.core.mail import send_mail


from app.models import *

from app.forms import *

# Create your views here.


def registration(request):
    
    EUMFO = UserMF()
    EPMFO = ProfileMF()
    d = {"EUMFO":EUMFO, "EPMFO": EPMFO}
    
    if request.method=='POST' and request.FILES:
        NMUFDO = UserMF(request.POST)
        NMPMFDO = ProfileMF(request.POST, request.FILES)

        if NMUFDO.is_valid() and NMPMFDO.is_valid():

            MUMFDO = NMUFDO.save(commit=False)
            pw = NMUFDO.cleaned_data['password']
            MUMFDO.set_password(pw)
            MUMFDO.save()
        
            MPMFDO = NMPMFDO.save(commit=False)
            MPMFDO.username = MUMFDO
            MPMFDO.save()
            
            send_mail(
                'Registration Successfull',
                 'your registration is successfull.',
                'amitchauhan6599@gmail.com',
                [MUMFDO.email],
                fail_silently=False,
            )
        
            return HttpResponse("Registrations is successfull")
        else:
            return HttpResponse('invalide')
    
    return render(request,"registration.html",d)



def dummy(request):
    return render(request,"dummy.html")



def Loginuser(request):
    if request.method =='POST':
        username = request.POST['username']
        password = request.POST['password']
        AUO = authenticate(request, username=username, password=password)
        if AUO:
            if AUO.is_active:
                login(request, AUO)
                request.session['username'] = username
                return HttpResponseRedirect(reverse('dummy'))
            else:
                return HttpResponse("Your account is not active")
        else:
            return HttpResponse("Invalid username or password")
    return render(request,"login.html")
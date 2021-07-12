from django.shortcuts import render
from .models import ClientEmail, Message

# Create your views here.

def Home(request):
    if request.method == "POST":
        firstName = request.POST.get("firstname")
        lastName = request.POSt.get("lastname")
        message = request.POST.get("message")
        email = request.POST.get("email")

        message = Message.objects.create(
            firstName = firstName,
            lastName = lastName,
            message = message,
            email = email
        )
        
        message.save()

        return render(request, 'Home/index.html')
    return render(request, 'Home/index.html')
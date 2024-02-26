from django.shortcuts import render,redirect
from django.contrib.auth import authenticate
from django.http import JsonResponse
from .models import login
from .serializer import loginserializer
# Create your views here.
def login_list(request):
    logins = login.objects.all()
    serializer = loginserializer(logins, many=True)
    return JsonResponse(serializer.data, safe=False)


def loginaction(request):
    usernames = request.POST.get("username")
    passwords = request.POST.get("password")
    if usernames and passwords:
        user = authenticate(request,username=usernames, password=passwords)
        if user is not None:
            loginserializer(request, user)
            return redirect(login_list)
        else:
            return render(request, 'loginhtml.html')
    else:
        return render(request, 'loginhtml.html')
    
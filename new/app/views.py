from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate,login
from .models import Qns
from django.contrib import messages
import random

# Create your views here.
def index(request):
    return render(request,"index.html")

def loginuser(request):
    return render(request,"login.html")

def userregister(request):
    if request.method == 'POST':
        uname = request.POST.get('name')
        email = request.POST.get('Email')
        passw = request.POST.get('epassword')
        cpasw= request.POST.get('confirm')
        if passw == cpasw:
            password = make_password(passw)
            user = User(username=uname,email=email,password = password)
            user.save()
            print("user created")
            return redirect(loginuser)

        else:
            return redirect(index)

def userauth(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        passw = request.POST.get('password')
        user = authenticate(request,username = uname,password = passw)
        if user is not None:
            login(request,user)
            return render(request,"qns.html")
        else:
            return redirect(loginuser)
def qnsgenerator(request):
    if request.method == 'POST':
        qns = request.POST.get('qns')
        ans = request.POST.get('ans')
        data = Qns(question=qns,answer=ans,user=request.user)
        data.save()
        return redirect(index)

def qns_render(request):
    
        question =Qns.objects.all()
        randomqns = random.choice(question)
        context = {
            'qns':randomqns
        }
        return render(request, 'ans.html',context = context)
def logoutuser(request):
    return redirect(index)

from django.shortcuts import redirect
from django.contrib import messages

def answers(request):
    if request.method == 'POST':
        ans = request.POST.get('ans')  # Get the submitted answer
        qns = request.POST.get('qns')  # Get the related question

        # Retrieve the question object from the database
        Qn = Qns.objects.filter(question=qns)  # Use filter for queryset

        if Qn.exists():  # Check if the question exists
            correct_answer = Qn[0].answer  # Get the correct answer
            if ans.strip().lower() == correct_answer.strip().lower():  # Compare case-insensitively
                messages.info(request, "Answer is correct")
            else:
                messages.info(request, "Answer is wrong")
        else:
            messages.error(request, "Question not found!")

        return redirect(qns_render)  # Make sure 'qns_render' is the correct URL name
    else:
        messages.error(request, "Invalid request method!")
        return redirect(qns_render)

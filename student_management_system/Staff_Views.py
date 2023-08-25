

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from app.models import Course,Session_Year,CustomUser,Student,Staff,Subject

def HOME(request):
    return render(request,'Staff/home.html')
from django.shortcuts import render

# Create your views here.
from app.models import *

def display_dept(request):

    LOE=Dept.objects.all()
    d={'details':LOE}

    return render(request,'display_dept.html',d)


def display_emp(request):
    LOE=Emp.objects.all()
    d={'employee':LOE}

    return render(request,'display_emp.html',d)


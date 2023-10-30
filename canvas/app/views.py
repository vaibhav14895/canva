from django.shortcuts import render
from app.models import Data

def home(request):
    dsa1 = Data.objects.values_list('dsa', flat=True)
    project1=Data.objects.values_list('project',flat=True)
    time1=Data.objects.values_list('date',flat=True)
    dsa=list(dsa1)
    project=list(project1)
    days_of_month = [date.day for date in time1]
    print(days_of_month)
    context={"DSA": dsa,
             "project":project,
             "dates":days_of_month
             }
    return render(request,"index.html",context)
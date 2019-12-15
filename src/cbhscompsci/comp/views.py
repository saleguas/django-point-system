from django.http import HttpResponse
from django.shortcuts import render
import os
from points.models import Student, MeetingKey, PointsEntry, hashStudentNo, MeetingEntry

def about(request):
    # return HttpResponse("about")
    return render(request, "about.html")

def index(request):
    return render(request, "index.html")
    # return HttpResponse("home")

def bingAuth(request):
    return render(request, 'BingSiteAuth.xml')
def googleAuth(request):
    return render(request, 'google225f06044a247783.html')
def gallery(request):
    path = "assets/gallery"
    folderArr = []
    nameArr = os.listdir(path)
    dirArr = []
    for year in nameArr:
        for file in os.listdir(os.path.join(path, year)):
            file = os.path.join("gallery", year, file)
            folderArr.append(file)

    context = {
        "folderNames" : nameArr,
        "folderFiles" : folderArr
    }
    return render(request, "gallery.html", context)

def meetings(request):

    context = {
        "meetings" : MeetingKey.objects.all()
    }
    return render(request, 'meetings.html', context)

def meetings_detail(request, pk):
    tMeeting = MeetingKey.objects.filter(id=pk).first()
    entrys = MeetingEntry.objects.filter(meeting=tMeeting)
    context = {
        "meeting" : tMeeting,
        "entrys" : entrys
    }
    return render(request, 'meetings_detail.html', context)

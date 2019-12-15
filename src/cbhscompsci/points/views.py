from django.shortcuts import render
from .models import Student, MeetingKey, PointsEntry, hashStudentNo
from django.http import HttpResponse
from .forms import PointsForm
from django.shortcuts import get_object_or_404
from django.utils.translation import ugettext_lazy as _
from django.core.exceptions import ValidationError
from django.contrib import messages
from itertools import groupby

monthRef = {
    8 : 'August',
    9 : 'September',
    10 : "October",
    11 : "November",
    12 : 'December',
    1 : 'January',
    2 : 'February',
    3 : 'March',
    4 : 'April',
    5 : 'May',
    6 : 'June'
}

def getStatus(v):
    if v < 10:
        return ['inactive', 'text-danger']
    elif v < 20:
        return ['average', 'text-warning']
    elif v < 30:
        return ['good', 'text-info']
    else:
        return ['spectacular', 'text-success']

# Create your views here.
def points_list(request):
    students = Student.objects.all().order_by("-points")
    context = {
        'students' : students,
        'topStudents' : students[:15]
    }
    return render(request, 'points/points_list.html', context)





def points_detail(request, id):
    student = Student.objects.get(id=id)
    totalPoints = 0
    for students in Student.objects.all():
        totalPoints += students.points;
    pointArr = PointsEntry.objects.filter(student=student).order_by('date')
    startMonth = pointArr.first().date.month
    endMonth = pointArr.last().date.month
    if endMonth <= 6:
        endMonth += 12
    lenn = endMonth - startMonth + 1
    points = [0]*lenn
    months = [""]*lenn
    colors = [""]*lenn
    for i in range(lenn):
        for x in pointArr:
            month = x.date.month
            if (month <= 6):
                month += 12
            if (month == startMonth + i):
                points[i] += x.points
        month = startMonth + i
        if (month > 12):
            month -= 12
        months[i] = monthRef[month]
        if points[i] < 10:
            colors[i] = "rgba(255, 99, 132,"
        elif points[i] < 20:
            colors[i] = "rgba(255, 206, 86,"
        elif points[i] < 30:
            colors[i] = "rgba(54, 162, 235,"
        else:
            colors[i] = "rgba(129, 247, 173,"

    avgPoints = (sum(points)/len(points))
    recentPoints = points[-1]
    avgStatus, avgColor = getStatus(avgPoints)[0], getStatus(avgPoints)[1]
    recentStatus, recentColor = getStatus(recentPoints)[0], getStatus(recentPoints)[1]
    avgPoints /= 40
    recentPoints /= 40
    avgPoints *= 100
    recentPoints *= 100

    context = {
        'totalPoints' : totalPoints,
        'student' : student,
        'pointArr' : pointArr,
        'months' : months,
        'points' : points,
        'colors' : colors,
        'avgPoints' : avgPoints,
        'recentPoints' : recentPoints,
        'avgStatus' : avgStatus,
        'recentStatus' : recentStatus,
        'avgColor' : avgColor,
        'recentColor' : recentColor

    }
    print(context)
    return render(request, 'points/points_detail.html', context)







def points_entrys(request):
    form = PointsForm(request.POST or None)
    query = request.GET.get('meetingKey')
    if query is not None:
        form.initial['meetingKey'] = query



    # Only do something if the request is post
    if request.method == "POST":
        form = PointsForm(request.POST)
        # Make sure noone is trying to hack us. Can use cleaned_data after calling is_valid
        if form.is_valid():
            # If the meetingkey is not valid then stop the program

            # Get the meetingKey object associated with the meeting key
            data = MeetingKey.objects.filter(meetingKey=form.cleaned_data['meetingKey'])
            if data.exists() == False:
                raise ValidationError(_('Key does not exist.'))
            # Startblock
            # We are going to check if a student exists. If it doesn't then we are going to create one
            formInput = form.cleaned_data
            newID = hashStudentNo(formInput['student_ID'])
            if Student.objects.filter(studentNo=newID).exists() == False:
                newID = hashStudentNo(formInput['student_ID'])
                newStudent = Student(studentNo=formInput['student_ID'], firstName=(formInput['firstName']).lower(), lastName=(formInput['lastName']).lower(), points=0)
                newStudent.save()
            # EndBlock
            # After creating the student, we will fetch it based on the inputted ID
            currentStudent = Student.objects.filter(studentNo=hashStudentNo(form.cleaned_data['student_ID'])).first()

            for object in PointsEntry.objects.filter(student=currentStudent):
                if object.meeting == data.first():
                    # raise ValidationError(_('Points already added.'))
                    return HttpResponse('Points already added.')

            messages.success(request, 'Request submitted succesfully!')
            form.save()
            form = PointsForm()
            # Save the form. Also adds a point entry
    context = {
        'form' : form,
    }
    return render(request, 'points/entry.html', context)

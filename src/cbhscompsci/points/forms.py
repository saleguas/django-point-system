from django import forms

from .models import Student, MeetingKey, PointsEntry, hashStudentNo, MeetingEntry
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator

class PointsForm(forms.Form):

    meetingKey = forms.CharField(
        validators=[RegexValidator(regex='^.{64}$', message='Length has to be 64', code='nomatch')],
        label="Meeting Key",
        required=True,
        widget=forms.TextInput(
            attrs={
                'class' :'form-control',
                'type' : 'password',
                'id' : 'inputPassword4',
                'placeholder' : 'Password'
                }
            )
        )
    student_ID = forms.CharField(
        validators=[RegexValidator(regex='^.{10}$', message='Length has to be 10', code='nomatch')],
        label="Student ID",
        required=True,
        widget=forms.TextInput(
            attrs={
                "type" : "text",
                "class" : "form-control",
                "id" : "InputID",
                "placeholder" : "0609067234"
            }
        )
    )
    firstName = forms.CharField(
        label="Last Name",
        required=True,
        widget=forms.TextInput(
            attrs={
                "type" : "text",
                "class" : "form-control",
                "id" : "firstName",
                "placeholder" : "John"
            }
        )
    )
    lastName = forms.CharField(
        label="Last Name",
        required=True,
        widget=forms.TextInput(
            attrs={
                "type" : "text",
                "class" : "form-control",
                "id" : "lastName",
                "placeholder" : "Smith"
            }
        )
    )

    def save(self):
        data = self.cleaned_data
        newID = hashStudentNo(data['student_ID'])
        print(newID)
        tMeeting = MeetingKey.objects.filter(meetingKey=data['meetingKey']).first()
        tStudent=Student.objects.filter(studentNo=newID).first()
        print(tStudent)
        newEntry = PointsEntry(student=tStudent, points=tMeeting.points, reason=tMeeting.name, meeting=tMeeting)
        print(newEntry)
        newEntry.save()
        meetingEntry = MeetingEntry(student=tStudent, meeting=tMeeting)
        meetingEntry.save()

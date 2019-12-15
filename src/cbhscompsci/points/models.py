from django.db import models
import hashlib
from django.urls import reverse
import qrcode
from django.core.files import File
from django.core.files.images import ImageFile
from django.conf import settings
import os
from django.contrib.sites.shortcuts import get_current_site

# Create your models here.
def hashKey():
    ck = CurrentKey.objects.first()
    print(ck)
    ck.currentKey = ck.currentKey + 1
    ck.save()
    return hashlib.sha256(str(ck.currentKey).encode('utf-8')).hexdigest()

def hashStudentNo(string):
    return hashlib.sha256(str(hashlib.sha256(str(string+"iwannabetheboshy").encode('utf-8')).hexdigest()+"donotdisturb").encode('utf-8')).hexdigest()

def makeQR(QRstring):
    qr = qrcode.QRCode(
        version=None,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )

    qr.add_data("/".join([settings.WEB_DIR, 'points', 'entry', '?meetingKey=' + QRstring]))
    qr.make(fit=True)
    img = qr.make_image()
    dest = os.path.join(settings.MEDIA_ROOT, 'media/', 'meetingKey/', QRstring + '.png')
    img.save(dest)
    img.close()
    return dest

class CurrentKey(models.Model):

    currentKey = models.IntegerField(default=10)

    def __str__(self):
        return 'Current Key: ' + str(self.currentKey)

class Student(models.Model):


    id = models.AutoField(primary_key=True)
    studentNo = models.TextField()
    firstName = models.TextField()
    lastName = models.TextField()
    points = models.IntegerField(default=0)

    def __str__(self):
        return self.firstName + " " +self.lastName



    def save(self, *args, **kwargs):
        newNo = hashStudentNo(self.studentNo)
        if len(self.studentNo) != len(newNo):
            self.studentNo = newNo

        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('points:breakdown', kwargs={'id' : self.id})






class MeetingKey(models.Model):
    meetingKey = models.CharField(max_length=64, default=hashKey)
    name = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    points = models.IntegerField(default=0)
    desc = models.TextField()
    qr_code = models.ImageField(upload_to='meetingKey/', blank=True)

    def save(self, *args, **kwargs):
        path = makeQR(self.meetingKey)
        self.qr_code = path
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('meetingList', kwargs={'pk' : self.id})


class MeetingEntry(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, null=True)
    meeting = models.ForeignKey(MeetingKey, on_delete=models.CASCADE, null=True)



class PointsEntry(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    points = models.IntegerField()
    reason = models.TextField()
    meeting = models.ForeignKey(MeetingKey, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return str(self.date) + "-" + str(self.student)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        relatedEntries = PointsEntry.objects.filter(student=self.student)
        self.student.points = sum([entry.points for entry in relatedEntries])
        self.student.save()

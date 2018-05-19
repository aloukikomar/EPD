from django.db import models
from datetime import datetime   
# Create your models here.
class panelpost(models.Model):
    cs = 'ComputerScience'
    it = 'i.t.'
    csit = 'cs&it'
    ec = 'Electrical'
    csitec = 'csitec'
    me ='mech'
    cv ='civil'
    mc = 'mech&civil'
    Al = 'all'
    placement='placement'
    notice='notice'
    li='list_of_students'
    cong='congractulations'
    branch = (
        (cs, 'CS'),
        (it, 'IT'),
        (csit, 'CS&IT'),
        (ec, 'EC'),
        (csitec, 'CS,IT&EC'),
        (me, 'MECHANICAL'),
        (cv, 'CIVIL'),
        (mc, 'MEC&CIVIL'),
        (Al, 'ALL'),
    )
    Branch = models.CharField(
        max_length=200,
        choices=branch,
        default=Al,
    )

    types = (
        (placement, 'placement'),
        (cong, 'congratulations'),
        (li, 'list_of_students'),
        (notice, 'notice'),
    
    )
    Type = models.CharField(
        max_length=200,
        choices=types,
        default=notice,
    )
    Username = models.CharField(max_length=140)
    College = models.CharField(max_length=140, default='Ipec')
    Title = models.CharField(max_length=140)
    Date = models.DateTimeField(default=datetime.now(), blank=True)
    DDate = models.DateTimeField(default=datetime.now(), blank=True)
    Subject = models.TextField(max_length=840)
    Markslow12 = models.IntegerField(default=0)
    Markslowb = models.IntegerField(default=0)
    Pack = models.IntegerField(default=0)
    Training = models.IntegerField(default=0)

    def __str__(self):
        return self.Title
class Notification(models.Model):
    UserName = models.CharField(max_length=140)
    Date = models.DateTimeField(default=datetime.now(), blank=True)
    Roll =  models.IntegerField(default=0)
    To = models.CharField(max_length=140,default="ipec")
    Message = models.CharField(max_length=1040)
    def __str__(self):
        return self.UserName

class Student(models.Model):
    cs = 'ComputerScience'
    it = 'i.t.'
    ec = 'Electrical'
    me ='mech'
    cv ='civil'
    Al = 'all'
    branch = (
        (cs, 'CS'),
        (it, 'IT'),
        (ec, 'EC'),
        (me, 'MECHANICAL'),
        (cv, 'CIVIL'),
        (Al, 'ALL'),
    )
    Name = models.CharField(max_length=140)
    rollno =  models.IntegerField(default=0) 
    Branch = models.CharField(
        max_length=200,
        choices=branch,
        default=Al,
    )
    
    Markslow12 = models.IntegerField(default=0)
    Markslowc = models.IntegerField(default=0)
    Markslowb = models.IntegerField(default=0)
    def __str__(self):
        return self.Name
    
class List(models.Model):
    cs = 'ComputerScience'
    it = 'i.t.'
    ec = 'Electrical'
    me ='mech'
    cv ='civil'
    Al = 'all'
    branch = (
        (cs, 'CS'),
        (it, 'IT'),
        (ec, 'EC'),
        (me, 'MECHANICAL'),
        (cv, 'CIVIL'),
        (Al, 'ALL'),
    )
    Branch = models.CharField(
        max_length=200,
        choices=branch,
        default=Al,
    )
    ListName = models.CharField(max_length=140)
    College = models.CharField(max_length=140, default='Ipec')
    Date = models.DateTimeField(default=datetime.now(), blank=True)

    Markslow12 = models.IntegerField(default=0)
    Markslowb = models.IntegerField(default=0)
    Markslowc = models.IntegerField(default=0)

    def __str__(self):
        return self.ListName
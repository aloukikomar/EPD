import login.models as m
from django.db import connection, transaction
cursor = connection.cursor()

def auth(id,passw):   
    cursor.execute("SELECT Password FROM Login_UserMain WHERE UserName ='"+id+"' AND Password ='"+passw+"'")
    row = cursor.fetchone()
    r= m.UserMain.objects.raw("select * from Login_UserMain where UserName ='"+id+"' AND Password ='"+passw+"'")
    return row

def mlist(id,passw):   
    cursor.execute("SELECT * FROM Main_students WHERE UserName ='"+id+"' AND Password ='"+passw+"'")
    row = cursor.fetchone()
    r= m.UserMain.objects.raw("select * from Login_UserMain where UserName ='"+id+"' AND Password ='"+passw+"'")
    return row
from django.http import HttpResponseRedirect
from django.shortcuts import render
import mysql.connector as sql
fn=''
ln=''
em=''
pwd=''
r=''

# Create your views here.

def signaction(request):
    global fn,ln,em,pwd,r
    if request.method == 'POST':
        m= sql.connect(host="localhost",user="root",password="Moumi@17#",database="website")
        cursor = m.cursor()
        d=request.POST
        for key, value in d.items():
            if key=="fname":
                fn=value
            if key=="lname":
                ln=value
            if key=="email":
                em=value
            if key=="password":
                pwd=value
            if key=="role":
                r=value
        c= "insert into users Values('{}','{}','{}','{}','{}')".format(fn,ln,em,pwd,r)
        cursor.execute(c)
        m.commit()
    return render(request,"F3.html")


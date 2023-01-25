from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.db.models import Q
from django.shortcuts import render, redirect

from libraryapp.models import Student, Course, Books, Issue_Book


def lof_fun(request):
    return render(request,'login.html',{'data':''})


def log_read_fun(request):
    user_name=request.POST['txtname']
    user_password=request.POST['txtpwrd']
    u=authenticate(username=user_name,password=user_password)
    if u is not None:
        if u.is_superuser:
            return render(request,'home.html')
        else:
            return render(request,'login.html',{'data':'Inavalid username or password'})
    elif Student.objects.filter(Q(Student_name=user_name) & Q(Student_password=user_password)).exists():
        request.session['name']=user_name
        return render(request,'home_stu.html',{'data':user_name})
    else:
        return render(request,'login.html',{'data':'username or password is invalid'})


def studentreg_fun(request):
    c=Course.objects.all()
    return render(request,'studentregister.html',{'data':'','course_data':c})


def student_read_fun(request):
    user=Student.objects.filter(Q(Student_name=request.POST['txtname']) & Q(Student_password=request.POST['txtpwrd']))
    if user:
        return render(request,'studentregister.html',{'data':'username and password already exists'})
    else:
        s = Student()
        s.Student_name = request.POST['txtname']
        s.Student_phno = request.POST['txtphno']
        s.Student_Sem = request.POST['txtsem']
        s.Student_password = request.POST['txtpwrd']
        s.Student_course = Course.objects.get(course_name=request.POST['ddlcourse'])
        s.save()
        return redirect('log')


def adminreg_fun(request):
    return render(request,'adminregister.html',{'data':''})


def adminreg_read_fun(request):
    u = authenticate(username=request.POST['txtname'], password=request.POST['txtpwrd'])
    if u is not None:
        if u.is_superuser:
            return render(request, 'AdminReg.html', {'data': 'Username and Password Already Exist'})
        else:
            u = User.objects.create_superuser(username=request.POST['txtname'], password=request.POST['txtpwrd'])
            u.save()
            return redirect('log')
    else:
        u = User.objects.create_superuser(username=request.POST['txtname'], password=request.POST['txtpwrd'])
        u.save()
        return redirect('log')


def addbook_fun(request):
    c=Course.objects.all()
    return render(request,'addbook.html',{'data':c})


def addbook_read_fun(request):
    b = Books()
    b.Book_name = request.POST['txtbname']
    b.Author_name = request.POST['txtauth']
    b.Course_id = Course.objects.get(course_name=request.POST['ddlcourse'])
    b.save()
    c = Course.objects.all()

    return render(request,'addbook.html',{'data':c,'msg':'one book added succefully'})


def display_fun(request):
    b=Books.objects.all()
    return render(request,'display.html',{'books':b})


def updatebook_fun(request,id):
    b=Books.objects.get(id=id)
    c=Course.objects.all()
    if request.method == "POST":
        b.Book_name = request.POST['txtbname']
        b.Author_name = request.POST['txtauth']
        b.Course_id = Course.objects.get(course_name=request.POST['ddlcourse'])
        b.save()
        c=Course.objects.all()
        return render(request,'updatebooks.html',{'course':c,'book':b,'msg':'one book updated succesfully'})
    return render(request,'updatebooks.html',{'course':c,'book':b,"msg":""})


def deletebook_fun(request,id):
    b=Books.objects.get(id=id)
    b.delete()
    return redirect('dis')


def assignbooks_fun(request):
    c = Course.objects.all()
    return render(request,'assign.html',{'data':c})


def readsemcourse_fun(request):
    stdsem = request.POST['txtsem']
    course = request.POST['ddlcourse']
    students = Student.objects.filter(Q(Student_Sem=stdsem) & Q(Student_course=Course.objects.get(course_name=course)))
    books = Books.objects.filter(Course_id=Course.objects.get(course_name=course))
    return render(request,'assign.html',{'students':students,'books':books})


def readstdbook_fun(request):
    ib=Issue_Book()
    ib.Student_Name=Student.objects.get(Student_name=request.POST['ddlstuname'])
    ib.Book_Name=Books.objects.get(Book_name=request.POST['ddlbkname'])
    ib.Start_date=request.POST['sdate']
    ib.End_date=request.POST['edate']
    ib.save()
    c=Course.objects.all()
    return render(request,'assign.html',{'course':c,'msg':"Book assignesd succesfully"})


def displaybook_fun(request):
    ibooks=Issue_Book.objects.all()
    return render(request,'displayissuedbook.html',{'ibooks':ibooks})


def updateibook_fun(request,id):
    ib=Issue_Book.objects.get(id=id)
    bk=Books.objects.all()
    if request.method=="POST":
        ib.Student_Name=Student.objects.get(Student_name=request.POST['txtname'])
        ib.Book_Name=Books.objects.get(Book_name=request.POST['ddlbkname'])
        ib.Start_date=request.POST['sdate']
        ib.End_date=request.POST['edate']
        ib.save()
        return redirect('disbooks')
    return render(request,'update.html',{'ib':ib,'books':bk})


def deleteibook_fun(request,id):
    ib = Issue_Book.objects.get(id=id)
    ib.delete()
    return redirect('disbooks')


def stubooks(request):
    ib=Issue_Book.objects.filter(Student_Name=Student.objects.get(Student_name=request.session['name']))
    print(ib)
    return render(request,'stdissuedbook.html',{'books':ib})


def stdhome(request):
    return render(request,'home_stu.html',{'data':request.session['name']})
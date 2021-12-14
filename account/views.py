from django.shortcuts import render, HttpResponseRedirect, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import *
from .models import *
from .decorator import *
from django.core.exceptions import PermissionDenied
from datetime import datetime
from datetime import date

global filternews
def filternews(queryfilter):
    try:
        newsdetails = News.objects.filter(dept=queryfilter).order_by('postedtime')
    except News.DoesNotExist:
        newsdetails = None
    filterednews = []
    if newsdetails is not None:
        for ND in newsdetails:
            if ND.status:
                filterednews.append({
                "id": ND.id,
                "headlines": ND.headlines,
                "details": ND.details,
                'dept': ND.dept,
                'owner': ND.owner,
                'img':ND.img,
                "postedtime": ND.postedtime
            })
            else:
                filterednews
    else:
        filterednews
        
    return filterednews


# Create your views here.
 
def index1(request):
    ec=News.objects.filter(dept='Electronics&Communication').order_by('postedtime')
    
    context={'ec':ec}
    return render(request,'site/index1.html',context)   
def ece1(request):
     #ece=News.objects.filter(dept='Electronics&Communication').order_by('postedtime')
    ece1=filternews('Electronics&Communication')
                
                
    context={'ece1':ece1}   
    return render(request,'site/ece1.html',context)  
def ee1(request):
        #ee=News.objects.filter(dept='Eltrecical').order_by('postedtime')
    ee1=filternews('Electrical')
    context={'ee1':ee1}
    return render(request,'site/ee1.html',context)  
def cse1(request):
       #cse=News.objects.filter(dept='ComputerScience').order_by('postedtime')
    cse1=filternews('ComputerScience')
    context={'cse1':cse1} 
    return render(request,'site/cse1.html',context) 
def me1(request):
        #me=News.objects.filter(dept='Mechanical').order_by('postedtime')
    me1=filternews('Mechanical')
    context={'me1':me1}
    return render(request,'site/me1.html',context)  
def ce1(request):
        #ce=News.objects.filter(dept='Civil').order_by('postedtime')
    ce1=filternews('Civil')
    context={'ce1':ce1}
    return render(request,'site/ce1.html',context)  
def about1(request):
    return render(request,'site/about1.html')  
def annualfest1(request):
    return render(request,'site/annualfest1.html') 
def blood1(request):
    return render(request,'site/blood1.html') 
def cdc1(request):
    return render(request,'site/cdc1.html') 
def dkb1(request):
    return render(request,'site/dkb1.html') 
def gargiday1(request):
    return render(request,'site/gargiday1.html') 
def infosis1(request):
    return render(request,'site/infosis1.html')
def leader1(request):
    return render(request,'site/leader1.html')
def mining1(request):
    return render(request,'site/mining1.html')
def pro1(request):
    return render(request,'site/pro1.html')
def radio1(request):
    return render(request,'site/radio1.html')
def ramt1(request):
    return render(request,'site/ramt1.html')  
def science1(request):
    return render(request,'site/science1.html')  
def sports1(request):
    return render(request,'site/sports1.html') 
def welder1(request):
    return render(request,'site/welder1.html') 
def women1(request):
    return render(request,'site/women1.html') 
def work1(request):
    return render(request,'site/work1.html')
  


# def detailsnews(request):
    
#     detailsnews=News.objects.filter(dept='detailsnews').order_by('postedtime')
    
#     context={'detailsnews':detailsnews}
#     return render(request, 'home/detailsnews.html',context) 

#  ('Mechanical', 'Mechanical'),
    # ('Civil', 'Civil'),
    # ('Electrical', 'Electrical'),
    # ('ComputerScience', 'Computer Science'),
    # ('Electronics&Communication', 'Electronics & Communication'),
#   ('Event', 'Event'),
#   ('CDC', 'CDC'),#

@OnlyAuth
def signin(request):
    LM = LoginForm(request.POST or None)
    if request.method == 'POST':
        if LM.is_valid():
            UserName = request.POST.get('username')
            PassWord = request.POST.get('password')
            user = authenticate(request, username=UserName, password=PassWord)

            if user is not None and user.is_cdc:
                login(request, user)
                return redirect('cdc')
            elif user is not None and user.is_teacher:
                login(request, user)
                return redirect('teacher')
            elif user is not None and user.is_student:
                login(request, user)
                return redirect('student')
            else:
                messages.error(request, 'Username or Password is incorrect')
        else:
            messages.error(request, LM.errors)
    else:
        LM = LoginForm()
    context = {'form': LM}
    return render(request, 'common/signin.html', context)


@OnlyAuth
def signup(request):
    if request.method == 'POST':
        SF = SignupForm(request.POST)
        if SF.is_valid():
            isStudent = True
            isTeacher = False
            if isStudent:
                SignUpUser = SF.save(commit=False)
                SignUpUser.is_student = True
                SignUpUser.status = True
                SignUpUser.save()
            elif isTeacher:
                SignUpUser = SF.save(commit=False)
                SignUpUser.is_teacher = True
                SignUpUser.status = False
                SignUpUser.save()
            else:
                messages.warning(request, 'Please Select Your user Type')
                return redirect('signin')
            user = SF.cleaned_data.get('username')
            messages.success(request, 'Account Created for ' + user)
            return redirect('signin')
        else:
            messages.error(request, SF.errors)
    else:
        SF = SignupForm()
    context = {'form': SF}
    return render(request, 'common/signup.html', context)


@login_required(login_url='signin')
def signout(request):
    logout(request)
    return redirect('index1')

@login_required(login_url='signin')
def cdc(request):
    if not request.user.is_cdc:
        raise PermissionDenied
    return render(request, 'admin/CdcProfile.html')


@login_required(login_url='signin')
def student(request):
    if not request.user.is_student:
        raise PermissionDenied
    if not request.user.status:
        return render(request, 'common/notActive.html')

    userdata = User.objects.get(pk=request.user.id)
    if request.method == 'POST':
        UserProfileForm = SignupForm(
            request.POST, request.FILES, instance=userdata)

        if UserProfileForm.is_valid():
            student = UserProfileForm.save(commit=False)
            student.is_student = True
            student.status = True
            UserProfileForm.save()
            messages.success(
                request, 'Profile is Updated. please login again to craete a new Session')
            return redirect('signout')
        else:
            messages.warning(request, UserProfileForm.errors)
    else:
        UserProfileForm = SignupForm(instance=userdata)
    context = {'StudentData': userdata, 'UserProfileForm': UserProfileForm}
    return render(request, 'student/StudentProfile.html', context)




# @login_required(login_url='signin')
# def cdc(request):
#     if not request.user.is_cdc:
#         raise PermissionDenied
#     return render(request, 'admin/CdcProfile.html')





@login_required(login_url='signin')
def addnews(request):
    if not request.user.status:
        return render(request, 'common/notActive.html')

    userdata = User.objects.get(pk=request.user.id)

    try:
        newsdetails = News.objects.filter(owner=request.user.id)
    except News.DoesNotExist:
        newsdetails = None

    AllNews = []
    if newsdetails is not None:
        for ND in newsdetails:
            user = User.objects.get(pk=ND.owner)
            if user is not None:
                author = user.first_name + ' ' + user.last_name
                img = user.profilepic.url
            else:
                author = ""

            AllNews.append({
                "id": ND.id,
                "headlines": ND.headlines,
                "details": ND.details,
                'dept': ND.dept,
                'owner': ND.owner,
                'ownername': author,
                'ownerimg': img,
                "postedtime": ND.postedtime,
            })

    if request.method == 'POST':
        NewsForm = NewsManagement(request.POST, request.FILES)
        if NewsForm.is_valid():
            news = NewsForm.save(commit=False)
            # image = Image.open(news.img) 
            # new_image = image.resize((800, 800))
            # news.img=new_image
            news.status = False
            news.owner = request.user.id
            news.postedtime = date.today()
            news.save()
            messages.success(
                request, 'Your News Details is submited and wait for CDC process')
            return redirect('allnews')
        else:
            messages.warning(request, NewsForm.errors)

    else:
        NewsForm = NewsManagement()

    context = {'StudentData': userdata, 'NewsData': newsdetails,
               'NewsForm': NewsForm}
    return render(request, 'news/addnews.html', context)


@login_required(login_url='signin')
def allnews(request):
    if not request.user.status:
        return render(request, 'common/notActive.html')

    userdata = User.objects.get(pk=request.user.id)
    try:
        newsdetails = News.objects.all()
    except News.DoesNotExist:
        newsdetails = None

    AllNews = []
    if newsdetails is not None:
        for ND in newsdetails:
            user = User.objects.get(pk=ND.owner)
            if user is not None:
                author = user.first_name + ' ' + user.last_name
                img = user.profilepic.url
            else:
                author = ""
              
            print(author)
              
            AllNews.append({
                "id": ND.id,
                "headlines": ND.headlines,
                "details": ND.details,
                'dept': ND.dept,
                'owner': ND.owner,
                'ownername': author,
                'ownerimg': img,
                "postedtime": ND.postedtime
            })
    context = {'StudentData': userdata, 'NewsData': AllNews}
    return render(request, 'news/Allnews.html', context)


@login_required(login_url='signin')
def editnews(request, pk):
    if not request.user.status:
        return render(request, 'common/notActive.html')

    userdata = User.objects.get(pk=request.user.id)
    newsdetails = News.objects.get(pk=pk)

    if request.method == 'POST':
        NewsForm = NewsManagement(
            request.POST, request.FILES, instance=newsdetails)
        if NewsForm.is_valid():
            news = NewsForm.save(commit=False)
            news.status = False
            news.owner = request.user.id
            news.postedtime = date.today()
            news.save()
            messages.success(
                request, 'Your News Details is submited')
            return redirect('allnews')
        else:
            messages.warning(request, NewsForm.errors)
    else:
        NewsForm = NewsManagement(instance=newsdetails)

    context = {'StudentData': userdata, 'NewsForm': NewsForm,'newsdetails':newsdetails}
    return render(request, 'news/editnews.html', context)


@login_required(login_url='signin')
def deletenews(request, pk):
    if not request.user.status:
        return render(request, 'common/notActive.html')
    if request.method == 'POST':
        target_data = News.objects.get(pk=pk)
        target_data.delete()
        messages.success(request, 'This News deleted')
        return redirect('allnews')


def newsdetails(request,pk):
    if not request.user.status:
        return render(request, 'common/notActive.html')

    userdata = User.objects.get(pk=request.user.id)
    try:
        newsdetails = News.objects.get(pk=pk)
    except News.DoesNotExist:
        newsdetails = None
     
    newsowner= User.objects.get(pk=newsdetails.owner)  
        

    
    context = {'StudentData': userdata, 'NewsData': newsdetails,'newsowner':newsowner}
    return render(request, 'news/newsdetails.html', context)
    

@login_required(login_url='signin')
def teacher(request):
    if not request.user.is_teacher:
        raise PermissionDenied
    if not request.user.status:
        return render(request, 'common/notActive.html')
    userdata = User.objects.get(pk=request.user.id)
    if request.method == 'POST':
        UserProfileForm = SignupForm(
            request.POST, request.FILES, instance=userdata)

        if UserProfileForm.is_valid():
            student = UserProfileForm.save(commit=False)
            student.is_teacher = True
            student.status = True
            UserProfileForm.save()
            messages.success(
                request, 'Profile is Updated. please login again to craete a new Session')
            return redirect('signout')
        else:
            messages.warning(request, UserProfileForm.errors)
    else:
        UserProfileForm = SignupForm(instance=userdata)
    context = {'StudentData': userdata, 'UserProfileForm': UserProfileForm}
    return render(request, 'teacher/TeacherProfile.html', context)



    






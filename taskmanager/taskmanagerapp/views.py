from django.shortcuts import render,redirect,get_object_or_404
from .models import task_manager_login,tasks
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
@csrf_exempt
def registerloginfunc(request):
        global lemail
        if request.method=='POST':
                lemail=request.POST.get('loginmail')
                lpass=request.POST.get('loginpass')
                rname=request.POST.get('regname')
                rmail=request.POST.get('regmail')
                rpass=request.POST.get('regpass')
                if rname != None:
                    if not task_manager_login.objects.filter(email=rmail).exists():
                            my_data = task_manager_login(name=rname,email=rmail,password=rpass)
                            my_data.save()
                if lemail != None:
                    if task_manager_login.objects.filter(email=lemail,password=lpass).exists():
                        return redirect(taskmanagerfunc)
        return render(request,'registerlogin.html')
def forgotpassfunc(request):
    if request.method=="POST":
        gotmail=request.POST.get('forgemail')
        if task_manager_login.objects.filter(email=gotmail).exists():
            got1pass=request.POST.get('newentpass1')
            got2pass=request.POST.get('newentpass2')
            if got1pass==got2pass:
                task_manager_login.objects.filter(email=gotmail).update(password=got1pass)
                return redirect(registerloginfunc)
    return render(request,'forgotpass.html')
def taskmanagerfunc(request):
      search=request.GET.get('searchvalue')
      sorting=request.GET.get('sort')
      register=task_manager_login.objects.get(email=lemail)
      alltasks=tasks.objects.filter(user=register)  
      if sorting:
           alltasks=alltasks.order_by(sorting)
      if request.method=='POST':
            title=request.POST.get('title')
            describe=request.POST.get('description')
            due=request.POST.get('duedate')
            priority=request.POST.get('prior')
            status=request.POST.get('status')
            insert=tasks(title=title,descr=describe,duedate=due,prior=priority,status=status,user=register)
            insert.save()
      if search:
        register=task_manager_login.objects.get(email=lemail)
        alltasks=tasks.objects.filter(user=register,title__icontains=search)
      return render(request,'taskmanager.html',{'alltasks':alltasks})
def update(request,id):
    sintask=tasks.objects.filter(id=id)
    if request.method == 'POST':
        status=request.POST.get('status')
        tasks.objects.filter(id=id).update(status=status)
        return redirect(taskmanagerfunc)
    return render(request,'updatetask.html',{'tasks':sintask})

def delete(request,id):
    if request.method=='POST':
          task=tasks.objects.filter(id=id)
          task.delete() 
          return redirect(taskmanagerfunc)
    return render(request,'delete.html')

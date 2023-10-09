from django.shortcuts import render , redirect
from django.http import HttpResponse
from .models import CLUB
from .forms import ProjectForm

def name(request):
    return HttpResponse("Hi This is Abrar")

def projects(request):
    return render(request,'projects/projects.html')

def wordcount(request):
    return render(request,'projects/wordcount.html')

def counter(request):
    words = request.POST['words']
    counter = len(words.split())
    return render(request,'projects/counter.html',{'count':counter})

def css(request):
    return render(request,'projects/css.html')

def clubs(request):
    proObjs = CLUB.objects.all()
    names = [obj.name for obj in proObjs]
    print('proObjs:', proObjs)
    return render(request, 'projects/clubs.html', {'names': names, 'proObjs': proObjs})

def createProject(request):
    form = ProjectForm()
    if request.method=='POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('projects')
    context ={'form':form}
    return render(request,"projects/project_form.html",context)

def updateProject(request,pk):
    project = CLUB.objects.get(name=pk)
    form = ProjectForm(instance=project)
    
    if request.method=='POST':
        form = ProjectForm(request.POST,request.FILES,instance=project)
        if form.is_valid():
            form.save()
            return redirect('projects')
    context ={'form':form}
    return render(request,"projects/project_form.html",context)

def deleteProject(request,pk):
    project=CLUB.objects.get(name=pk)
    if request.method=='POST':
        project.delete()
        return redirect('projects')
    context={'object': project}
    return render(request,"projects/delete.html",context)
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserform
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Project, Survey
from .forms import SurveyForm, ProjectForm
from rest_framework import generics
from .serializers import TodoSerializer
from django.contrib import messages

# Create your views here.



class DetailTodo(generics.RetrieveAPIView):
        queryset = Survey.objects.all()
        serializer_class = TodoSerializer

class ListTodo(generics.ListAPIView):
        queryset = Survey.objects.all()
        serializer_class = TodoSerializer

def register(request):
    form = CreateUserform()
    
    if request.method == 'POST':
        form = CreateUserform(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account created successfully for '+ user)
            # Redirect to a success page or any other desired page
            return redirect('login')  # Replace 'success_page_name' with the actual name or URL of your success page
    
    context = {'form': form}
    return render(request, 'survey/registration.html', context)
    

def LoginPage(request):
    if request.method =='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user =authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, "Username or Password is incorrect")
    context={}
    
    return render(request, 'survey/login.html',context)

def LogoutUser(request):
    logout(request)
    return redirect('login')
 
@login_required(login_url='login')  
def Home(request):
    projects = Project.objects.all()
    total_proj = Project.objects.count()
    filtered_projects = Project.objects.filter(users=request.user)
    
    form = ProjectForm()

    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save(commit=True, user=request.user)
            messages.success(request, 'Project created successfully')
            return redirect('home')
    
    context = {
        'projects': projects,
        'total_proj': total_proj,
        'form': form,
        'filtered_projects': filtered_projects
    }
    
    return render(request, 'survey/home.html', context)

def Surveypage(request):
    
    form = SurveyForm()
    if request.method =='POST':
        form = SurveyForm(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect('home')
    
    context = {'form':form}
    
    return render(request, 'survey/survey_form.html', context)


def ProjPage(request):
    project = Project.objects.all()
    survey = Survey.objects.all()
    total_surveys = Survey.objects.count()
    
    context={
        'project':project,
        'survey':survey,
        'total_surveys':total_surveys,
    }
    return render(request, 'survey/proj.html', context)


def ProjFIl(request, pk):    
    project = Project.objects.get(id=pk)
    form = ProjectForm(instance=project)
    if request.method == 'POST':
        form = ProjectForm(request.POST, instance=project)
        if form.is_valid():
            form.save()
            return redirect('home')
    
    context={'form':form}
    return render(request, 'survey/projForm.html',context)

def ProView(request,pk):
    project = Project.objects.get(id=pk)
    survey = Survey.objects.all()
    form= SurveyForm()
    if request.method == 'POST':
        form = SurveyForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Survey Saved Successfully')
            return redirect('home')
    context={
        'project':project,
        'survey':survey,
        'form':form,
    }
    return render(request, 'survey/projView.html', context)


def DeleteProj(request, pk):    
     prod= Project.objects.get(id=pk)
         
     if request.method =='POST':
        prod.delete()
        return redirect('home')
    
     context = {'prod':prod}
     return render(request, 'survey/delete.html', context)
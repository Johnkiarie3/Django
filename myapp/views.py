from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader  # for routing your templates
from django.contrib.auth.forms import UserCreationForm
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.csrf import csrf_protect
from  .models import Client
from django.shortcuts import redirect



def home(request):
    template= loader.get_template('home.html')
    return HttpResponse(template.render())

def login(request):
    template = loader.get_template('login.html')
    return HttpResponse(template.render())

def services(request):
    template = loader.get_template('services.html')
    return HttpResponse(template.render())

def about_us(request):
    template = loader.get_template('about_us.html')
    return HttpResponse(template.render())
def dashboard(request):
  data=Client.objects.all()
  context={'data':data}
  return render(request,'dashboard.html',context)

def courses(request):
    template = loader.get_template('courses.html')
    return HttpResponse(template.render())


@csrf_exempt
def addClient(request):
    if request.method=='POST':
        name=request.POST.get('Fullname')
        email=request.POST.get('Email')
        age=request.POST.get('Age')
        quantity=request.POST.get('services')
        payment=request.POST.get('payment')

    obj1=Client(name=name, email=email, age=age, quantity=quantity, payment=payment)
    obj1.save()

    mydata = Client.objects.all();
    context = {'data': mydata}
    return render(request, 'dashboard.html', context)

def editClient(request,id):
    data=Client.objects.get(id=id)
    context = {'data': data}
    return render(request, 'updateClient.html', context)

def updateClient(request,id):
    if request.method=='POST':
        name=request.POST.get('Fullname')
        email=request.POST.get('Email')
        age=request.POST.get('Age')
        quantity=request.POST.get('services')
        payment=request.POST.get('payment')

        #modifying the client details based on the client id given
        editClient = Client.objects.get(id=id)
        editClient.name=name
        editClient.email=email
        editClient.age=age
        editClient.quantity=quantity
        editClient.payment=payment
        editClient.save()
    return redirect('/dashboard')

def deleteClient(request, id):
    deleteClient=Client.objects.get(id=id)
    deleteClient.delete()
    return redirect('/dashboard')

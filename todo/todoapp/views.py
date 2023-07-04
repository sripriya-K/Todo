from django.shortcuts import render, redirect
from todoapp.forms import MyForm
from todoapp.models import Notes
# Create your views here.
def homePage(request):
    return render(request,'home.html')

def addNotes(request):
    sample = MyForm(request.POST or None)
    if sample.is_valid():
        sample.save()
        return redirect('/')
    return render(request,'add.html',{'sap':sample})

def viewNotes(request):
    data = Notes.objects.all()#[{},{},{}] 
    return render(request,'notes.html',{'notes':data})
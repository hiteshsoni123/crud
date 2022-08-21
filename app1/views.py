from django.shortcuts import render, HttpResponseRedirect
from .forms import StudentRegistration
from .models import User
from django.contrib import messages

def add_show(request):
    if request.method == 'POST':
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            pw = fm.cleaned_data['password']
            reg = User(name=nm, email=em, password=pw)
            reg.save()
            messages.success(request, 'Added!')
            fm = StudentRegistration()
    else:
        fm = StudentRegistration()
    stu = User.objects.all()
    return render(request, 'addandshow.html', {'form':fm, 'stu':stu})

def update(request, id):
    if request.method == 'POST':
        pi = User.objects.get(pk=id)
        fm = StudentRegistration(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
            messages.info(request, 'Updated!')

    else:
        pi = User.objects.get(pk=id)
        fm = StudentRegistration(instance=pi)       
    return render(request, 'updates.html', {'form':fm})


def delete(request, id):
    if request.method == 'POST':
        pi = User.objects.get(pk=id)
        pi.delete()
        messages.info(request, 'Deleted!')
        return HttpResponseRedirect('/')
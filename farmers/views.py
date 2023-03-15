from django.shortcuts import render, redirect
from .forms import ActivityForm, FarmerOneForm, UrbanFarmerForm

def welcome(request):
    return render(request, 'welcome.html')

def add_fo(request):
    form = FarmerOneForm
    context = {'form': form}
    if request.method == 'POST':
        form = FarmerOneForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_fo')
    return render(request, 'farmers/add_fo.html', context)

def add_uf(request):
    form = UrbanFarmerForm
    if request.method == 'POST':
        form = UrbanFarmerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_uf')
    context = {'form': form}
    return render(request, 'farmers/add_uf.html', context)

def add_activity(request):
    form = ActivityForm
    if request.method == 'POST':
        form = ActivityForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_activity')
    context = {'form': form}
    return render(request, 'farmers/add_activity.html', context)

def dashboard(request):
    return render(request, 'dashboard.html')
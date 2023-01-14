from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import database
# Create your views here.
name = ""
def index(request):
    # if(request.method == 'post'):
    #     acc = request.POST.get('acc')
    #     pin = request.POST.get('pin')
    #     refer = database.objects.get(pk = acc)
    #     if(refer.count() > 0):
    return render(request, 'index.html')
        
    # return render(request, 'verify.html')
def addMoney(request):

    amount = request.POST.get('amount')

    return render(request, 'add.html')
def withdrawMoney(request):
    return render(request, 'withdraw.html')
def checkMoney(request):
    params = {}
    if(request.method == 'POST'):
        acc = request.POST.get('acc')
        obj = database.objects.get(pk = acc)
        print(acc)
        params['balance'] = obj.balance
        return render(request, 'check.html', params)
    return render(request, 'check.html')
def about(request):
    return render(request, 'about.html')

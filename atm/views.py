from django.shortcuts import render, redirect
from django.http import HttpResponse
from service.models import database

# Create your views here.
name = ""
# def verify(request):
    # if request.method == "POST":
    #     acc = request.POST.get('acc')
    #     pin = request.POST.get('pin')
    #     obj = database.objects.get(accountNumber = acc)
    # return render(request, 'verify.html', {'verified':False})
def index(request):
    # if request.method == 'POST':
    #     acc = request.POST.get('acc')
    #     pin = request.POST.get('pin')
    #     refer = database.objects.get(pk = acc)
        

    return render(request, 'index.html')
        
    # return render(request, 'verify.html')
def addMoney(request):
    if request.method == "POST":

        acc = request.POST.get('acc')
        amount = request.POST.get('amount')
        print(f"{acc}                       {amount}")
        obj = database.objects.get(accountNumber = acc)
        balance = int(obj.balance)
        balance += int(amount)
        obj.balance = str(balance)
        obj.save() 
    return render(request, 'add.html')
def withdrawMoney(request):
    if request.method == "POST":
        acc = request.POST.get('acc')
        amount = request.POST.get('amount')
        obj = database.objects.get(pk = acc)
        balance = int(obj.balance)
        balance -= amount
        obj.balance = str(balance)
        obj.save()
    return render(request, 'withdraw.html')
def checkMoney(request):
    params = {}
    if request.method == 'POST':
        acc = request.POST.get('acc')
        obj = database.objects.get(accountNumber = acc)
        print(obj)
        params['balance'] = obj.balance
        params['note'] = 'The balance for the acc number ' + acc + ' is \n'
        return render(request, 'check.html', params)
    return render(request, 'check.html')
def about(request):
    return render(request, 'about.html')
def test(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        pin = request.POST.get('pin')
        accno = request.POST.get('acc')
        bal = request.POST.get('balance')
        obj = database()
        print(name)
        obj.name = name
        obj.accountNumber = accno
        obj.pin = pin
        obj.balance = bal
        obj.save()
        return render(request, 'test.html')
    return render(request, 'test.html')
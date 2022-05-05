from django.shortcuts import redirect, render
from main.models import AddPerson
from django.db.models import Q
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def mainfn(request):
    return render(request,"index.html")
def master(request):
    return render(request,"master.html")
def add(request):
    if request.method == 'POST':
        name = request.POST['name']
        hName = request.POST['hname']
        sName = request.POST['sname']
        post = request.POST['post']
        place = request.POST['place']
        dist = request.POST['dist']
        state = request.POST['state']
        pin = request.POST['pin']
        address = AddPerson(name=name,hName=hName,sName=sName,post=post,place=place,dist=dist,state=state,pin=pin)
        address.save()
        return render(request,"addperson.html",{"status":"your address added successfully"})
    else:
        return render(request,"addperson.html")

# @csrf_exempt
# def search(request):
#     if request.method == 'POST':
#         search = request.POST['search']
#         search_address = AddPerson.objects.filter(Q(name__icontains=search) | Q(sName__icontains=search))
#         print(search_address)
#         return render(request,'search.html',{'search':search_address})
#     else:
#         return redirect('search')

@csrf_exempt
def search(request):
    if request.method == 'POST':
        search = request.POST['search']
        if search!="":
            search_address = AddPerson.objects.filter(Q(name__icontains=search) | Q(sName__icontains=search))
            print(search_address)
            if search_address.exists():
                return render(request,'search.html',{'search':search_address})
            else:
                return render(request,"index.html",{'msg':'no result found'})
        else:
            return redirect('search')
    else:
        return redirect('search')




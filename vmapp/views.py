from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import SignUpForm,VehicleDtlsForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import User, Group
from .models import VehicleDtls
import json
from django.http import JsonResponse


@login_required(login_url="/login")
def index(request):
    item_id = request.POST.get("item-id")
    addform = VehicleDtlsForm()
    VehicleDtlsDisplay = VehicleDtls.objects.all().order_by("-id")

    if item_id:
            item = VehicleDtls.objects.filter(id=item_id).first()
            if item and request.user.has_perm("vmapp.delete_VehicleDtls"):
                item.delete()

    return render(request, 'vmapp/index.html',{"add_form": addform,"VehicleDtlsDisplay":VehicleDtlsDisplay})



def sign_up(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)  
            if form.data['user_mode']=="3":
                user.is_staff = True  
            elif form.data['user_mode']=="1":
                user.is_superuser = True  
            else:
                pass

            user.save()  
            if form.data['user_mode']=="3":
                my_group = Group.objects.get(name='User') 
                my_group.user_set.add(user)
            elif form.data['user_mode']=="2":
                my_group = Group.objects.get(name='Admin') 
                my_group.user_set.add(user)
            else:
                pass
            login(request, user)
            return redirect('/index')
    else:
        form = SignUpForm()

    return render(request, 'registration/sign_up.html', {"form": form})


@login_required(login_url="/login")
@permission_required("vmapp.add_VehicleDtls", login_url="/login", raise_exception=True)
def add_vehicle_dtls(request):
    is_ajax = request.headers.get('X-Requested-With') == 'XMLHttpRequest'
    if is_ajax and request.method == "POST":
        form = VehicleDtlsForm(request.POST)
        if form.is_valid():
            VehicleDtls = form.save(commit=False)
            VehicleDtls.author = request.user
            VehicleDtls.save()
            return JsonResponse({"Sucess": True}, status=200)
        else:
            return JsonResponse({"error": form.errors}, status=400)
            
    return JsonResponse({"error": ""}, status=400)



@login_required(login_url="/login")
def update(request,id):
    context = {}
    object=VehicleDtls.objects.get(id=id)
    form=VehicleDtlsForm(instance=object) 
    if request.method == 'POST':
        form = VehicleDtlsForm(request.POST,instance=object)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form_edit':form}
    return render(request,'vmapp/update.html',context)





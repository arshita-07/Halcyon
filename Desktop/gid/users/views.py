from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import *
from .models import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate , login, logout
from django.contrib.auth.decorators import user_passes_test


def Client_check(user):
    return user.is_Client

def Hospital_check(user):
    return user.is_Hospital

def login_main(request):
    return render(request,'LoginMain.html')

def signup_main(request):
    return render(request,'users/signup_main.html')

# Create your views here.
def register(request):
    uerror = ""
    werror = "" 
    if request.method=='POST':
        u_form = UserRegisterForm(request.POST)
        w_form = ClientRegisterForm(request.POST, request.FILES)
        if u_form.is_valid() and w_form.is_valid():
            user = u_form.save()
            user.first_name = u_form.cleaned_data['first_name']
            user.last_name = u_form.cleaned_data['last_name']
            user.is_Client = True
            user.save()
            uname = u_form.cleaned_data.get('username')
            messages.success(request, f'Account created for {uname}!')
            wuser = w_form.save(commit=False)
            wuser.user=user
            wuser.save()
            return redirect('login_main')
        else:
            uerror = u_form.errors
            werror = w_form.errors
    else:
        u_form = UserRegisterForm()
        w_form = ClientRegisterForm()
    return render(request,'Signup.html',{'u_form':u_form,'w_form':w_form,'uerror':uerror,'werror':werror})


def Hospital_register(request):
    uerror = ""
    rerror = ""
    if request.method=='POST': 
        u_form = UserRegisterForm(request.POST)
        r_form = HospitalRegisterForm(request.POST, request.FILES)
        if u_form.is_valid() and r_form.is_valid():
            user = u_form.save()
            user.first_name = u_form.cleaned_data['first_name']
            user.last_name = u_form.cleaned_data['last_name']
            user.is_Hospital = True
            user.save()
            uname = u_form.cleaned_data.get('username')
            messages.success(request, f'Account created for {uname}!')
            ruser = r_form.save(commit=False)
            ruser.user=user
            ruser.save()
            return redirect('login_main')
        else:
            uerror = u_form.errors
            rerror = r_form.errors
    else:
        u_form = UserRegisterForm()
        r_form = HospitalRegisterForm()
    return render(request,'Hospital_signup.html',{'u_form':u_form,'r_form':r_form,'uerror':uerror,'rerror':rerror})

def admin_register(request):
    uerror = ""
    aerror = ""
    if request.method=='POST':
        u_form = UserRegisterForm(request.POST)
        a_form = AdminRegisterForm(request.POST, request.FILES)
        if u_form.is_valid() and a_form.is_valid():
            user = u_form.save()
            user.first_name = u_form.cleaned_data['first_name']
            user.last_name = u_form.cleaned_data['last_name']
            user.is_admin = True
            user.save()
            uname = u_form.cleaned_data.get('username')
            messages.success(request, f'Account created for {uname}!')
            auser = a_form.save(commit=False)
            auser.user=user
            auser.save()
            return redirect('login_main')
        else:
            uerror = u_form.errors
            aerror = a_form.errors
    else:
        u_form = UserRegisterForm()
        a_form = AdminRegisterForm()
    return render(request,'users/admin_signup.html',{'u_form':u_form,'a_form':a_form,'uerror':uerror,'aerror':aerror})


@login_required
def update_profile_Client(request):
    if request.user.is_Client:
        uerror=""
        werror=""
        if request.method == 'POST':
            u_uform = UserUpdateForm(request.POST,instance = request.user)
            w_uform = ClientUpdateForm(request.POST, request.FILES, instance=request.user.Client_user)
            if u_uform.is_valid() and w_uform.is_valid():
                u_uform.save()
                w_uform.save() 
                messages.success(request, f'profile updated !')
                return redirect('Client_profile')
            else:
                uerror = u_uform.errors
                werror = w_uform.errors
                w_uform.save()
                
        else:
            u_uform = UserUpdateForm(instance = request.user)
            w_uform = ClientUpdateForm(instance = request.user.Client_user)
        return render(request,'Profile.html',{'u_uform':u_uform,'w_uform':w_uform,'werror':werror,'uerror':uerror})
    else:
        return redirect('eh')


@login_required
def update_profile_admin(request):
    if request.user.is_admin:
        if request.method == 'POST':
            u_uform = UserUpdateForm(request.POST,instance = request.user)
            a_uform = AdminUpdateForm(request.POST, request.FILES, instance=request.user.admin_user)
            if u_uform.is_valid() and a_uform.is_valid():
                u_uform.save()
                a_uform.save()
                messages.success(request, f'profile updated !')
                return redirect('admin_profile')
            else:
                uerror = u_uform.errors
                aerror = a_uform.errors
        else:
            u_uform = UserUpdateForm(instance = request.user)
            a_uform = AdminUpdateForm(instance = request.user.admin_user)
        return render(request,'users/profile_admin.html',{'u_uform':u_uform,'a_uform':a_uform})
    else:
        return redirect('eh')

@login_required
def update_profile_Hospital(request):
    if request.user.is_Hospital:
        if request.method == 'POST':
            u_uform = UserUpdateForm(request.POST,instance = request.user)
            r_uform = HospitalUpdateForm(request.POST, request.FILES, instance=request.user.Hospital_user)
            if u_uform.is_valid() and r_uform.is_valid():
                u_uform.save()
                r_uform.save() 
                messages.success(request, f'profile updated !')
                return redirect('Hospital_profile')
            else: 
                uerror = u_uform.errors
                rerror = r_uform.errors
        else:
            u_uform = UserUpdateForm(instance = request.user)
            r_uform = HospitalUpdateForm(instance = request.user.Hospital_user)
        return render(request,'Profile_Hospital.html',{'u_uform':u_uform,'r_uform':r_uform})
    else:
        return redirect('eh')

def Hospital_login(request):
    if request.method == 'POST':
        r_lform = HospitalLoginForm(request.POST)
        if r_lform.is_valid():
            uname = r_lform.cleaned_data.get('username')
            pwd = r_lform.cleaned_data.get('password')
            user= authenticate(username=uname, password=pwd)
            if user is not None:
                print(user.is_Hospital)
                if user.is_Hospital:
                    x = Hospital.objects.get(user=user)
                    if x.verified:
                        login(request, user)
                        return redirect('home')
                    else:
                        return redirect('verification_wait')
                else:
                    messages.warning(request, f'You account does not have access to Hospital login since it is not a Hospital account')
                
            else:
                messages.warning(request, f'Invalid credentials please retry')
    else:
        r_lform = HospitalLoginForm()
    return render(request, 'Hospital_login.html',{'r_lform':r_lform})

def verification_wait_view(request):
    return render(request, 'Verification_wait.html')

def admin_login(request):
    if request.method == 'POST':
        a_lform = AdminLoginForm(request.POST)
        if a_lform.is_valid():
            uname = a_lform.cleaned_data.get('username')
            pwd = a_lform.cleaned_data.get('password')
            user= authenticate(username=uname, password=pwd)
            if user is not None: 
                if user.is_admin:
                    login(request, user)
                    return redirect('home')
                else:
                    messages.warning(request, f'You account does not have access to Admin login since it is a basic_user account')
            else:
                messages.warning(request, f'Invalid credentials please retry')
    else:
        a_lform = AdminLoginForm()
    return render(request, 'Admin_login.html',{'a_lform':a_lform})


@login_required
def change_status(request,pk):
    r = Hospital.objects.get(id=pk)
    if request.user.is_admin:
        if r.verified:
            r.verified = False
            r.save()
            return redirect('Hospital_request')
        else:
            r.verified = True
            r.save()
            return redirect('Hospital_request')
    else:
        return redirect('eh') 

def eh_view(request):
    return render(request,'eh.html')

@login_required
def Hospital_request_view(request):
    if request.user.is_admin:
        Hospitals = Hospital.objects.all()
        return render(request,'users/Hospital_request.html',{'Hospitals':Hospitals})
    else:
        return redirect('eh')
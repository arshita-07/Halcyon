from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin , UserPassesTestMixin
from app.models import *
from django.http import HttpResponse
from django import forms
from .forms import *
from django.contrib.auth.decorators import login_required
from gid.settings import EMAIL_HOST_USER, BASE_DIR
from django.core.mail import send_mail
from django.contrib import messages
from django.core.mail import EmailMessage
from users.models import *


# Create your views here.

def home(request):
    return render(request,'Home.html')

def done(request):
    return render(request,'Done.html')

@login_required
def apply(request, pk):
    resource = Resource.objects.get(pk=pk)
    user = request.user
    if Application.objects.filter(resource=resource, applicant=user.Client_user):
        return redirect('done')
    else:
        if user.is_Client:
            if request.method == 'POST':
                application_form = Medical_History(request.POST , request.FILES)
                if application_form.is_valid():
                    application = application_form.save(commit=False)
                    application.applicant = user.Client_user
                    application.resource = resource
                    application.save()
                    resource.applicants.add(user.Client_user)
                    resource.save()
                    return redirect('myapplications')
            else:
                application_form = Medical_History()
        else:
            return redirect('eh')
        return render(request,'Apply.html',{'resource':resource,'user':user,'form':application_form})

@login_required
def myapplications(request):
    user = request.user
    if user.is_Client:
        applications=Application.objects.filter(applicant=user.Client_user)
        return render(request,'Applications.html',{'applications':applications})
    else:
        return redirect("eh")

@login_required
def applicationforresource(request,pk):
    if request.user.is_Hospital:
        resource = Resource.objects.get(pk=pk)
        applications = Application.objects.filter(resource = resource)
        return render(request,'Afj.html',{'applications':applications,'resource':resource})
    else:
        return redirect('eh')
    

class ResourceListView(ListView):
    model = Resource
    template_name = 'Resource_list.html'
    context_object_name ='resources'
    ordering = ['-date_posted']

class ResourceDetailView(DetailView):
    model = Resource
    context_object_name ='resource'
    template_name = 'Resource_detail.html'

class ResourceUpdateView(UserPassesTestMixin ,LoginRequiredMixin, UpdateView):
    model = Resource
    fields = ['title','resource_description','quantity','available_deadline','keywords','status','price']

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['available_deadline'].widget = forms.DateInput(attrs={'type':'date'})
        return form

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        resource = self.get_object()
        if self.request.user == resource.Hospital.user:
            return True
        else:
            return False

class ResourceCreateView(LoginRequiredMixin,UserPassesTestMixin, CreateView):
    model = Resource
    template_name="resource_form.html"
    fields = ['title','resource_description','quantity','available_deadline','keywords','status','location','price']

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['available_deadline'].widget = forms.DateInput(attrs={'type':'date'})
        return form

    def form_valid(self, form):
        form.instance.Hospital = self.request.user.Hospital_user
        return super().form_valid(form)

    def test_func(self):
        if self.request.user.is_Hospital:
            return True
        else:
            return False

class ResourceDeleteView(UserPassesTestMixin ,LoginRequiredMixin, DeleteView):
    model = Resource
    success_url = '/app/resource_list'

    def test_func(self):
        resource = self.get_object()
        if self.request.user == resource.Hospital.user:
            return True
        else:
            return False
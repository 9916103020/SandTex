from django.http import HttpResponse
from django.shortcuts import render,HttpResponseRedirect, HttpResponse
from .forms import RegistrationForm
import os
import shutil
from django.core.files.storage import FileSystemStorage
import requests
#from bs4 import BeautifulSoup
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
@csrf_protect
def my_code(request):
    if request.method == 'GET':
        if 'code' in request.GET:
            code = request.GET['code']
            with open('minor.tex', 'w') as the_file:
                the_file.write(code)
            # doSomething with pieFact here...
        return HttpResponse('success') # if everything is OK
    # nothing went well
    return HttpResponse('FAIL!!!!!')

@login_required
def profile(request):
    args ={'user' : request.user}
    return render(request,'editor2.html')

def home(request):
    return render(request,'Minor Project.html')

def about(request):
    return render(request,'aboutus.html')

@login_required
def compile(request):
    os.system("pdflatex minor.tex")
    os.remove('minor' + '.aux')
    os.remove('minor' + '.log')
    os.remove('static/minor.pdf')
    shutil.move("minor.pdf", "static/")
    return HttpResponse('success')

def pdf_viewer(request):
    #os.system("python preview.py")
    return HttpResponse('success')



@login_required
def editor(request):
    return render(request, 'editor2.html')

#def login(request):
#    return render(request,'login.html')

@login_required
def logout(request):
    return render(request,'logout.html')

def choice(request):
    return render(request,'accounts/choice.html')

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'accounts/choice.html')
                # return HttpResponseRedirect('/choice/')
        else:
            return HttpResponseRedirect('/error/')
    else:
        form= RegistrationForm(request.POST)

        args = {'form': form}
    return render(request, 'accounts/reg_form.html',args)

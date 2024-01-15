
from django.http import HttpResponse
from .models import Project
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.core.exceptions import ValidationError
from django.contrib import messages





def navbar(request):
   return render(request,'navbar.html')

def home(request):
   return render(request,'home.html')

def about(request):
   return render(request,'about.html')
def services(request):
   return render(request,'services.html')



def  viewRegistration(request):
   return render(request,'viewregistrations.html') 


def contact(request):
   return render(request,'contact.html')



# @login_required
# def welcome(request):
#     user = request.user
#     first_name = 'Guest'

#     # Check if the user has a related Project instance
#     if hasattr(user, 'project') and user.project:
#         first_name = user.project.firstname

#     return render(request, 'welcomepage.html', {'first_name': first_name})


def welcome(request):
   return render(request, 'welcomepage.html')


def registration(request):
   
   if request.method=='POST':
      firstname=request.POST['firstname']
      secondname=request.POST['secondname']
      email=request.POST['email']
      date = request.POST['date']
      try:
            date = Project._meta.get_field('date').to_python(date)
      except ValidationError as e:
            messages.error(request, f'Invalid date format: {e.message}')
            return render(request, 'registration.html')
      

      username = request.POST['username']
      password = request.POST['password']
      pincode= request.POST['pincode']
      # address=request.POST['address']
      
      user = User.objects.create_user(username=username, password=password)
      m=Project(firstname=firstname,email=email,date=date,secondname=secondname,user=user,pincode=pincode)
      m.user
      m.save()
      return redirect('home')
   return render(request,'registration.html')



def viewreg(request):
   post=Project.objects.all()
   return render(request,"viewregistrations.html",{"post":post})



def incorrect(request):
   return render(request,"incorrect.html")



# Your other import statements and views...
def login_view(request):
    print("Login view called")  # Add this line
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        print(f"Username: {username}, Password: {password}")  # Add this line

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            print("User authenticated successfully")
            return redirect('welcome')
        else:
            print("Invalid username or password")
            return render(request, 'incorrect.html', {'error_message': 'Invalid username or password'})

    return render(request, 'incorrect.html')


# Other views...    


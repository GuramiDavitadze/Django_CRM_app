from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm
from .models import Record
# დავარენდერეთ home.html ფაილი
def home(request):
    records = Record.objects.all()
    
    
    # Check to see if logging in
    if request.method=='POST':
        username=request.POST['username']
        password = request.POST['password']
        # Authenticate
        user = authenticate(request, username=username,password=password)
        if user is not None:
            login(request, user)
            messages.success(request,'You Have Been Logged In!')
            return redirect('home')
        else:
            messages.success(request, 'There Was An Error Logging In, Please Try Again...')
            return redirect('home')
    else:
        
        return render(request,'home.html',{'records':records})

def logout_user(request):
    logout(request)
    messages.success(request,"You have been logged out")
    return redirect('home')

def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            
            #Authenticate and login
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username,password=password)
            login(request,user)
            messages.success(request,'You have Successfully Registered!')
            return redirect('home')
        
    else:
        form = SignUpForm()
        return render(request,'register.html',{'form':form})
    return render(request,'register.html',{'form':form})

# pk - primary key
def costumer_record(request,pk):
    if request.user.is_authenticated:
        # Look Up Record
        costumer_record = Record.objects.get(id=pk)
        return render(request,'record.html',{'costumer_record':costumer_record})
    else:
        messages.success(request,'You must be logged in to view page!')
        return redirect('home')
    
def delete_record(request,pk):
    if request.user.is_authenticated:
        delete_it = Record.objects.get(id=pk)
        delete_it.delete()
        messages.success(request,"Record Deleted Successfully...")
        return redirect('home')
    else:
        messages.success(request,"You must be logged in to delete")
        return redirect('home')
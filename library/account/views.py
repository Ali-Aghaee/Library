from django.shortcuts import render,redirect
from .forms import SignupForm,LoginForm,UserInfoForm
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.decorators import login_required

# Create your views here.
def Signup(request):
    form = SignupForm()
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
                   
    content = {'form':form}
    return render(request, 'signup.html', content)

def Login(request):
    form = LoginForm()
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect('book_list')
        
    content = {'form':form}
    return render(request,'login.html',content)         


@login_required(login_url='login')          
def Logout(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
def UserInfo(request):
    form = UserInfoForm(initial={'username':request.user.username,
                                 'first_name':request.user.first_name,
                                 'last_name':request.user.last_name,
                                 'email':request.user.email})
    if request.method == 'POST':
        form = UserInfoForm(data=request.POST, instance=request.user)
        if form.is_valid():
            form.save()
    return render(request, 'user_info.html',{'form':form})
    
    
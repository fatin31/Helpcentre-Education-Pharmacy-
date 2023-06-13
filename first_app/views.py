from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import  render, redirect
from django.contrib.auth import login
from django.contrib import messages

from django.contrib.auth import login, authenticate,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import User
from .models import Diabetics
from .models import Otc
from .models import BabyCare
from .models import WomenChoice
from .models import PersonalCare
from .models import SWellness
from .models import CheckOut
from django.views import View
from .models import Cart

@login_required(login_url="login/")
def index(request):
    diction = {'title':"Index"}
    return render(request, 'index.html', context=diction)
@login_required(login_url="login/")
def index(request):

    return render(request, 'index.html',)

def sign_up(request):
    if request.method == 'POST':
        firstname = request.POST.get('fname')
        lastname = request.POST.get('lname')
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        
            
        user = User.objects.create_user(
                first_name=firstname,
                last_name=lastname,
                username=username,
                password=password,
                email=email
            )
        user.save()
        return redirect('login/')
        print(firstname,username,email)
    return render(request, 'Sign_up.html', )


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, 'Logged in successfully.')
            return redirect('index')
        else:
            messages.error(request, 'Invalid email or password.')
            return redirect('login/')

    return render(request, 'login.html')

def user_logout(request):
    logout(request)
    return redirect('login/')


def education(request):
    diction = {}
    return render(request, 'education.html', context=diction)
def eduList(request):
    diction = {}
    return render(request, 'edulist.html', context=diction)
def Dhaka(request):
    diction = {}
    return render(request, 'dhaka.html', context=diction)
def Khulna(request):
    diction = {}
    return render(request, 'khulna.html', context=diction)
def Rangpur(request):
    diction = {}
    return render(request, 'rangpur.html', context=diction)
def Barishal(request):
    diction = {}
    return render(request, 'barishal.html', context=diction)
def Chittagong(request):
    diction = {}
    return render(request, 'chittagong.html', context=diction)
def Mymensingh(request):
    diction = {}
    return render(request, 'mymensingh.html', context=diction)
def Rajshahi(request):
    diction = {}
    return render(request, 'rajshahi.html', context=diction)
def Sylhet(request):
    diction = {}
    return render(request, 'sylhet.html', context=diction)



def Pharmacy(request):
    diction = {}
    return render(request, 'pharmacy.html', context=diction)
def Diabetic(request):
    diction = {}
    return render(request, 'diabetics.html', context=diction)
def Diabetic(request):
    diabetics = Diabetics.objects.all()
    return render(request, 'diabetics.html', { 'diabetics':diabetics})

def otc(request):
    diabetics = Otc.objects.all()
    return render(request, 'otc.html', { 'diabetics':diabetics})

def babycare(request):
    diabetics = BabyCare.objects.all()
    return render(request, 'babycare.html', { 'diabetics':diabetics})
def womenchoice(request):
    diabetics = WomenChoice.objects.all()
    return render(request, 'women.html', { 'diabetics':diabetics})

def personalcare(request):
    diabetics = PersonalCare.objects.all()
    return render(request, 'personal.html', { 'diabetics':diabetics})

def wellness(request):
    diabetics = SWellness.objects.all()
    return render(request, 'swellness.html', { 'diabetics':diabetics})

def search_results(request):
    query = request.GET.get('query')

    if not query:
        return render(request, 'search_results.html', {'results': []})

    results = Diabetics.objects.filter(name__icontains=query)

    return render(request, 'search_results.html', {'results': results})


def add_to_cart(request):
    user=request.user
    diabetics = Diabetics.objects.all()
    return render(request,'addtocart.html.',{ 'add_to_cart':add_to_cart} )
def quick_test(request):
    diction = {}
    return render(request, 'Quickcheck.html', context=diction)

def show_cart(request):
    user=request.user
    cart= Cart.objects.filter(user=user)
    return render(request,'addtocart.html',locals())

def Order(request):
    user=request.user
    diabetics = Diabetics.objects.all()
    return render(request,'ordernow.html.',{ 'order':Order} )

def create_paypal_order(request):
    # Add your logic for creating the PayPal order here
    return HttpResponse("PayPal order created successfully")


def checkout (request):
    if request.method=='POST':
        name=request.POST.get('name')
        cardnumber=request.POST.get('cardnumber')
        expiration=request.POST.get('expiration')
        cvv=request.POST.get('cvv')
        number=request.POST.get('number')

        data1=CheckOut()
        data1.name=name
        data1.cardnumber=cardnumber
        data1.expiration=expiration
        data1.cvv=cvv
        data1.number=number
        data1.save()
        print(name,cardnumber,expiration,cvv,number)
        return redirect('confirm/')
    return render(request,'ordernow.html')

def orderlist (request):
    meet=CheckOut.objects.all()
    context={
        'data':meet,
    }
    return render(request,'confirm.html',context)


def confirm(request):
    diction = {}
    return render(request, 'confirm.html', context=diction)


# Create your views here.

from django.shortcuts import render
from groundapp.models import Contact, Customer, Owner
from groundapp.forms import ContactForm, CustomerForm, OwnerForm

# Create your views here.


def index(request):
    return render(request, "index.html", {})


def about(request):
    return render(request, "about.html", {})


def gallery(request):
    return render(request, "gallery.html", {})


def events(request):
    return render(request, "events.html", {})


def contact(request):
    return render(request, "contact.html", {})


def single(request):
    return render(request, "single.html", {})


def players(request):
    return render(request, "players.html", {})


def insert_contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            print("errors:", form.errors)
        return render(request, "contact.html", {"msg": "message sent"})
    return render(request, "contact.html", {"msg": ""})


# Customer views

def reg(request):
    if request.method == 'POST':
        print("hi")
        email = request.POST['email']
        if Customer.objects.filter(email=email).exists():
            print("email taken")
            return render(request, "customer_registration.html", {"msg": "email already exists"})
        else:
            form = CustomerForm(request.POST)
            print(form.errors)
            if form.is_valid():
                form.save()
                return render(request, "customer_registration.html", {"msg": "inserted sucess", "form": form})
            else:
                return render(request, "customer_registration.html", {})
    else:
        customer = CustomerForm()
        return render(request, "customer_registration.html", {"msg": "", "form": customer})


def customer_register(request):
    return render(request, "customer_registration.html", {})


def customer_login(request):
    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["password"]
        print(email, "", password)
        user = Customer.objects.filter(email=email, password=password,)
        if user.exists():
            request.session['email'] = email
            return render(request, "customer_home.html", {"msg": email})
        else:
            return render(request, "customer_login.html", {"msg": "email or password is not exist"})
    return render(request, "customer_login.html", {"msg": ""})


# owner views

def owner_reg(request):
    if request.method == 'POST':
        print("hi")
        email = request.POST['email']
        if Owner.objects.filter(email=email).exists():
            print("email taken")
            return render(request, "owner_registration.html", {"msg": "email already exists"})
        else:
            form = OwnerForm(request.POST,request.FILES)
            print(form.errors)
            if form.is_valid():
                form.save()
                return render(request, "owner_registration.html", {"msg": "inserted success", "form": form})
            else:
                return render(request, "owner_registration.html", {})
    else:
        owners = OwnerForm()
        return render(request, "owner_registration.html", {"msg": "", "form": owners})


def owner_register(request):
    return render(request, "owner_registration.html", {})


def owner_login(request):
    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["password"]
        print(email, "", password)
        user = Owner.objects.filter(email=email, password=password)
        if user.exists():
            request.session['email'] = email
            return render(request, "owner_home.html", {"msg": email})
        else:
            return render(request, "owner_login.html", {"msg": "email or password not exists"})
    return render(request, "owner_login.html", {"msg": ""})






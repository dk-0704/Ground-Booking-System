from django.shortcuts import render, redirect
from groundapp.models import Contact, Customer, Owner
from groundapp.forms import ContactForm, CustomerForm, OwnerForm
from ownerapp.models import Add_Ground
from customerapp.models import Book_slot
from customerapp.forms import Book_slotForm
from datetime import datetime

# Create your views here.


def customer_home(request):
    return render(request, "customer_home.html", {})


def customer_is_login(request):
    if request.session.__contains__("email"):
        return True
    else:
        return False


def customer_change_password(request):
    if customer_is_login(request):
        if request.method == "POST":
            email = request.session["email"]
            password = request.POST["password"]
            newpassword = request.POST["newpassword"]
            try:
                user = Customer.objects.get(email=email, password=password)
                user.password = newpassword
                user.save()
                msg = 'password update successfully'
                return render(request, "customer_login.html", {"msg": msg})
            except:
                msg = 'invalid data'
                return render(request, "customer_change_password.html", {"msg": msg})
        return render(request, "customer_change_password.html", {})
    else:
        return render(request, "customer_login.html", {})


def customer_logout(request):
    if request.session.has_key('email'):
        del request.session['email']
    return render(request, "customer_login.html.", {"msg": ""})


def customer_edit(request, email):
    customer = Customer.objects.get(email=email)
    return render(request, "customer_edit.html", {"customer": customer})


def customer_update(request):
    if request.method == 'POST':
        email = request.POST["email"]
        customers = Customer.objects.get(email=email)
        form = CustomerForm(request.POST, instance=customers)
        print(form.errors)
        if form.is_valid():
            form.save()
        return render(request, 'customer_home.html', {"msg": "updated"})
    return render(request, 'customer_edit.html', {})


def customer_details(request):
    email = request.session["email"]
    customer = Customer.objects.get(email=email)
    print(email)
    return render(request, "customer_details.html", {"customer": customer})


def customer_delete(request, email):
    customer = Customer.objects.get(email=email)
    customer.delete()
    return redirect("/customer_registration")


def grounds(request):
    view = Add_Ground.objects.all()
    return render(request, "grounds.html", {"views": view})


def ground_booking(request, id):
    email = request.session['email']
    customer = Customer.objects.get(email=email)
    ground = Add_Ground.objects.get(id=id)
    print("hi")
    if request.method == 'POST':
        bookslot = Book_slotForm(request.POST)
        time = request.POST["time"]
        date = request.POST["date"]
        hour = request.POST["hours"]
        #t = datetime.strptime(time, '%M:%S')
        #print(time,hour,type(time),type(hour),t,type(t))
        if Book_slot.objects.filter(time=time, date=date).exists():
            print(bookslot.errors)
            return render(request,"book.html",{"msg1":"This ground is already booked at the given date  slot. Please try another slot :)",
                                               "msg2":"This ground is already booked at the given time slot. Please try another slot :)",
                                               "id": ground.id, "customer": customer.id, "ground": ground.address, "cost": ground.cost})
        elif bookslot.is_valid():
            bookslot.save()
            return render(request, "book.html", {"msg": "success", "id": ground.id, "customer": customer.id, "ground": ground.address, "cost": ground.cost})
    return render(request, "book.html", {"id": ground.id, "customer": customer.id, "ground": ground.address, "cost": ground.cost})


def view_bookings(request):
    email = request.session["email"]
    customers = Customer.objects.get(email=email)
    booked = Book_slot.objects.filter(customer_id=customers.id)
    return render(request, "view_bookings.html", {"booked": booked})



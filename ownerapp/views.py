from django.shortcuts import render, redirect
from groundapp.models import Owner
from groundapp.forms import OwnerForm
from ownerapp.forms import Add_Ground
from ownerapp.forms import Add_GroundForm
from customerapp.models import Book_slot

# Create your views here.


def owner_home(request):
    return render(request, "owner_home.html", {})


def owner_is_login(request):
    if request.session.__contains__("email"):
        return True
    else:
        return False


def owner_change_password(request):
    if owner_is_login(request):
        if request.method == "POST":
            email = request.session["email"]
            password = request.POST["password"]
            newpassword = request.POST["newpassword"]
            try:
                user = Owner.objects.get(email=email, password=password)
                user.password = newpassword
                user.save()
                msg = 'password update successfully'
                return render(request, "owner_login.html", {"msg": msg})
            except:
                msg = 'invalid data'
                return render(request, "owner_change_password.html", {"msg": msg})
        return render(request, "owner_change_password.html", {})
    else:
        return render(request, "owner_login.html", {})


def owner_logout(request):
    if request.session.has_key('email'):
        del request.session['email']
    return render(request, "owner_login.html", {"msg": ""})


def owner_edit(request, email):
    owner = Owner.objects.get(email=email)
    return render(request, "owner_edit.html", {"owner": owner})


def owner_update(request):
    if request.method == 'POST':
        email = request.POST["email"]
        owners = Owner.objects.get(email=email)
        form = OwnerForm(request.POST, instance=owners)
        print(form.errors)
        if form.is_valid():
            form.save()
        return render(request, 'owner_home.html', {"msg": "updated"})
    return render(request, 'owner_edit.html', {})


def owner_details(request):
    email = request.session["email"]
    owner = Owner.objects.get(email=email)
    print(email)
    return render(request, "owner_details.html", {"owner": owner})


def owner_delete(email):
    owner = Owner.objects.get(email=email)
    owner.delete()
    return redirect("/owner_registration")


def add_grounds(request):
    email = request.session["email"]
    owner = Owner.objects.get(email=email)
    print("hii")
    if request.method == 'POST':
        print("hi2")
        add_ground = Add_GroundForm(request.POST, request.FILES)
        print(add_ground.errors)
        if add_ground.is_valid:
            print("errors:", add_ground.errors)
            add_ground.save()
            return render(request, "add_grounds.html", {"msg": "ground is posted", "id": owner.id})
    return render(request, "add_grounds.html", {"id": owner.id})


def view_grounds(request):
    email = request.session["email"]
    owner = Owner.objects.get(email=email)
    view = Add_Ground.objects.filter(owner_id=owner.id)
    return render(request, "view_ground.html", {"views": view})


def ground_edit(request, id):
    owner = Add_Ground.objects.get(id=id)
    return render(request, "ground_edit.html", {"user": owner, "id": owner.id,})


def ground_delete(request, id):
    owner = Add_Ground.objects.get(id=id)
    owner.delete()
    return render(request, "owner_home.html", {"owner": owner})


def ground_update(request):
    global id
    email = request.session["email"]
    owner = Owner.objects.get(email=email)
    if request.method == 'POST':
        id = request.POST["id"]
        grounds = Add_Ground.objects.get(id=id)
        grounds = Add_GroundForm(request.POST, request.FILES, instance=grounds)
        print(grounds.errors)
        if grounds.is_valid():
            grounds.save()
            grounds = Add_Ground.objects.filter(owner_id=owner.id)
        return render(request, 'ground_edit.html', {"msg": "updated", "owner": grounds, "id": owner.id})
    return render(request, 'ground_edit.html', {"id": owner.id})


def booked_slots(request, id):
    customer = Book_slot.objects.filter(ground_id=id)
    global booked_id
    booked_id=id
    return render(request, "booked_slot.html", {"customer": customer})


def booking_approve(request, book_id):
    approve = Book_slot.objects.get(id=book_id)
    approve.status = 1
    approve.save()
    return redirect('/booked_slots/'+str(booked_id))


def booking_reject(request, book_id):
    reject = Book_slot.objects.get(id=book_id)
    reject.status = 2
    reject.save()
    return redirect('/booked_slots/'+str(booked_id))



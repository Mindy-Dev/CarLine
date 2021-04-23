from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *
import bcrypt


# INDEX
def index(request):
    return render(request, 'riders/index.html')


# REGISTER
def register(request):
    errors = User.objects.register_validator(request.POST)

    if len(errors):
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    else:
        user = User.objects.create(
        first_name=request.POST['first_name'],
        last_name=request.POST['last_name'],
        email=request.POST['email'],
        password=bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()).decode())
        request.session['user_id'] = user.id
        request.session['greeting'] = user.first_name
        return redirect('/riders')


# LOGIN
def login(request):
    errors = User.objects.login_validator(request.POST)
    if len(errors):
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    else:
        user = User.objects.get(email=request.POST['login_email'])
        request.session['user_id'] = user.id
        request.session['greeting'] = user.first_name
        return redirect('/riders')


# SHOW ALL RIDERS FOR ONE PARENT - this needs to pass an ID
def all_riders(request):
    if "user_id" not in request.session:
        return redirect('/riders')
    else:
        context = {
            'all_riders': Rider.objects.all(),
            'current_user': User.objects.get(id=request.session['user_id'])
        }
        return render(request, 'riders/all_riders.html', context)


# CREATE
def add_rider(request):
    if 'user_id' not in request.session:
        return redirect('/')

    if request.method == "POST":
        errors = Rider.objects.rider_validator(request.POST)

        if len(errors):
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/riders/create')
        else:
            rider = Rider.objects.create(
            first_name = request.POST['first_name'],
            last_name = request.POST['last_name'],
            studentID = request.POST['studentID'],
            school_name = request.POST['school_name'],
            carID = request.POST['carID'],
            teacher = request.POST['teacher'],
            grade = request.POST['grade'],
            status = request.POST['status'],
            added_by = User.objects.get(id=request.session["user_id"]))
            messages.success(request, "Rider added!")
            return redirect('/riders')
    return redirect('/riders/all_riders')

# RENDERING THE FORM
def create(request):
    return render(request, 'riders/add_rider.html')

#SHOW ONE PARENT'S RIDERS
def show_one(request, rider_id):
    context = {
        'rider': Rider.objects.get(id=rider_id),
        'current_user': User.objects.get(id=request.session['user_id'])
    }
    return render(request, "riders/show_one.html", context)

#PICK UP - Parents click to pickup and rider is moved to the Waiting Line
def pickup(request, rider_id):
    rider = Rider.objects.get(id=rider_id)
    rider.status = "waiting"
    rider.save()
    return redirect('/riders')

#CARLINE
# def carline(request):
#     rider = Rider.objects.get(id=request.POST['rider_id'])
#     carline = Carline.objects.get(id=1)
#     carline.add(rider)
#     return redirect('/riders')

#CARLINE RENDER
def carline(request):
    riders = Rider.objects.filter(status= 'waiting')
    context = {
        "all_riders": riders
    }
    return render(request, 'school/carline.html', context)


#LOGOUT
def logout(request):
    request.session.clear()
    return redirect('/')

#WAITING - When parents click PICKUP, rider auto moved to this line/table
#Then the school can select which line/table to move rider
# def waiting(request, rider_id):
#     rider = Rider.objects.get(id=rider_id)
#     return redirect('/')

# #SEE ONE RIDER
# def show_rider(request, rider_id):
#     if 'user_id' not in request.session:
#         return redirect('/')
#     riders_with_id = Rider.objects.filter(id=rider_id)
#     if len(riders_with_id) == 0:
#         return redirect('/riders/all_riders')
#     context = {
#         'one_rider': Rider.objects.get(id=rider_id)
#     }
#     return render(request, "riders/all_riders.html", context)

# UPDATE USER ACCOUNT
# def update_user(request, user_id):
#     if request.method == 'POST':
#         errors = User.objects.register_validator(request.POST)
#     if errors:
#         for key, value in errors.items():
#             messages.error(request, value)
#         return redirect('/')
#         # process form
#     else:
#         hashed_pw = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()).decode()
#         print(hashed_pw)
#             #return the form
#         user = User.objects.get(id=user_id)
#         user.first_name = request.POST['first_name']
#         user.last_name = request.POST['last_name']
#         user.email = request.POST['email']
#         user.password = request.POST['password']
#         user.save()
#         return redirect('/riders')

# UPDATE RIDER INFO
# def update_rider(request, rider_id):

#         rider = Rider.objects.get(id=rider_id)
#         rider.rider_first_name = request.POST['first_name']
#         rider.rider_last_name = request.POST['last_name']
#         rider.rider_school_name = request.POST['rider_school_name']
#         rider.rider_carID = request.POST['rider_carID']
#         rider.rider_teacher = request.POST['rider_teacher']
#         rider.rider_grade = request.POST['rider_grade']
#         rider.save()
#         return redirect('/riders')

     # if request.method == 'POST':
    #     errors = Rider.objects.rider_validator(request.POST)
    # if errors:
    #     for key, value in errors.items():
    #         messages.error(request, value)
    #     return redirect('/')
    #     # process form
    # else:
    #     hashed_pw = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()).decode()
    #     print(hashed_pw)
            #return the form
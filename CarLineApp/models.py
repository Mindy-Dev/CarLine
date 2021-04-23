from django.db import models
from datetime import datetime
import re
from django.db.models.deletion import CASCADE
from django.http import request
# from django.db.models.deletion import CASCADE
import bcrypt

EMAIL_REGEX = re.compile(
    '^[_a-z0-9-]+(.[_a-z0-9-]+)@[a-z0-9-]+(.[a-z0-9-]+)(.[a-z]{2,4})$')


class UserManager(models.Manager):
    def register_validator(self, postData):
        errors = {}
        check = User.objects.filter(email=postData['email'])
        if len(postData['first_name']) < 2:
            errors['first_name'] = "First name must be at least 2 characters long."
        if len(postData['last_name']) < 2:
            errors['last_name'] = "Last name must be at least 2 characters long."
        if len(postData['password']) < 8:
            errors['password'] = "Password cannot be less than 8 characters."
        elif postData['password'] != postData['confirm_password']:
            errors['password'] = "Passwords do not match."
        if len(postData['email']) < 1:
            errors['reg_email'] = "Email address cannot be blank."

        elif not EMAIL_REGEX.match(postData['email']):
            errors['reg_email'] = "Please enter a valid email address."
        elif check:
            errors['reg_email'] = "Email address is already registered."
        return errors

    def login_validator(self, postData):
        errors = {}
        check = User.objects.filter(email=postData['login_email'])
        if not check:
            errors['login_email'] = "Email has not been registered."
        else:
            if not bcrypt.checkpw(postData['login_password'].encode(), check[0].password.encode()):
                errors['login_email'] = "Email and password do not match."
        return errors
        
# USERS = PARENTS AND SUPERS
class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    password = models.CharField(max_length=255)
    super = models.BooleanField(default=False)

    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    objects = UserManager()

class RiderManager(models.Manager):
    def rider_validator(self, reqPOST):
        errors = {}

        if len(reqPOST['first_name']) < 1:
            errors['first_name'] = "Please enter the student's first name."

        if len(reqPOST['last_name']) < 1:
            errors['last_name'] = "Please enter the student's last name."

        if len(reqPOST['studentID']) < 6:
            errors['studentID'] = "Please enter the student's 6-digit student ID."

        if len(reqPOST['school_name']) < 3:
            errors['school_name'] = "Please enter the school name."

        if len(reqPOST['carID']) < 1:
            errors['carID'] = "Please enter your student's car rider number."

        if len(reqPOST['teacher']) < 2:
            errors['teacher'] = "Please enter the rider's homeroom teacher (last name only)."

        if len(reqPOST['grade']) < 1:
            errors['grade'] = "Please enter the grade for this rider."
        return errors

class Carline(models.Model):
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

class Rider(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    studentID = models.IntegerField()
    school_name = models.CharField(max_length=255)
    carID = models.IntegerField()
    teacher = models.CharField(max_length=255)
    grade = models.IntegerField()
    added_by = models.ForeignKey(User, related_name="added_riders", on_delete=models.CASCADE)
    status = models.CharField(max_length=25)
    carline = models.ForeignKey(Carline, related_name="riders", on_delete=models.CASCADE, null=True)

    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    objects = RiderManager()



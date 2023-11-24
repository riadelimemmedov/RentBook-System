#

#!Django methods and Functions
from django.db.models import Q
from django.contrib import messages

import apps.account.models


#
#!Python modules and functions
from datetime import datetime


# *setFullName
def setFullName(name, surname):
    return f"{name} {surname}"


# *isExistsAccount
def isExistsAccount(email, phone):
    account = apps.account.models.Account.objects.filter(
        Q(email=email) | Q(phone=phone)
    ).first()

    if account:
        if account.email == email:
            return {
                "is_exists": True,
                "field": "email",
                "message_type": "info",
                "message_text": "Email already exists.",
            }
        if account.phone == phone:
            return {
                "is_exists": True,
                "field": "phone",
                "message_type": "info",
                "message_text": "Phone already exists.",
            }
    return {"is_exists": False}


# *createUser
def createUser(first_name, last_name, gender, account_type, email, phone, password):
    is_exists_account = isExistsAccount(email, phone)
    if is_exists_account.get("is_exists") == False:
        user = apps.account.models.Account.objects.create_user(
            first_name=first_name,
            last_name=last_name,
            gender=gender,
            account_type=account_type,
            email=email,
            phone=phone,
            password=password,
        )
        user.save()
        return {
            "message_type": "success",
            "message_text": "Registration successfull.",
            "user": user,
        }
    else:
        return is_exists_account


# ?Regex Pattern List
domain_pattern = r"^[\w\.-]+@[\w\.-]+\.(ru|com|az|org|net|edu|gov|mil|io|co|me|info|biz|tv|online|store|xyz)$"
body_pattern = "^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$"
phone_number_pattern = "994\s?\d{2}[2-9]\d{6}"

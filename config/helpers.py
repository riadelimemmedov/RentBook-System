#
#!Python modules and functions
from datetime import datetime


#?setFullName
def setFullName(name,surname):
    return f"{name} {surname}"


#?Regex Pattern List
domain_pattern = r'^[\w\.-]+@[\w\.-]+\.(ru|com|az|org|net|edu|gov|mil|io|co|me|info|biz|tv|online|store|xyz)$'
body_pattern = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$' 
phone_number_pattern = "994\s?\d{2}[2-9]\d{6}"
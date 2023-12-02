#

#!Celery
from celery import shared_task


#!Django
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import EmailMessage


#!Apps
import apps


# ?activateAccount
@shared_task(queue="tasks")
def activateAccount(**kwargs):
    pk = kwargs.get("pk")
    domain = kwargs.get("domain")
    account = apps.account.models.Account.objects.get(pk=pk)    

    print('Ay blett doamin gelde aqqq ', domain)
    
    print('Token is celery ', default_token_generator.make_token(account))

    mail_subject = "Please activate your account!"
    message = render_to_string(
        "account/account_verification.html",
        {
            "account": account,
            "domain": domain,
            "uid": urlsafe_base64_encode(force_bytes(account.pk)),
            "token": default_token_generator.make_token(account),
        },
    )
    to_email = account.email
    send_email = EmailMessage(mail_subject, message, to=[to_email])
    result = send_email.send()
    print("Result activate ", result)
    return True

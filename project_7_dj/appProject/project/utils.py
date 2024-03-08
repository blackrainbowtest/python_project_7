import random
import string

# email send
from django.core.mail import EmailMessage, EmailMultiAlternatives
# template to string for email
from django.template.loader import render_to_string
from django.shortcuts import render


def code_generator(size=6, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def create_shortcode(instance, size=6):
    new_code = code_generator(size=size)
    PasswordRecovery = instance.__class__
    print(type(PasswordRecovery))
    qs_exists = PasswordRecovery.objects.filter(shortcode=new_code).exists()
    if qs_exists:
        return create_shortcode(size=size)
    return new_code


def update_shortcode(instance, size=6):
    new_code = code_generator(size=size)
    PasswordRecovery = instance
    print(type(PasswordRecovery))
    qs_exists = PasswordRecovery.objects.filter(shortcode=new_code).exists()
    if qs_exists:
        return create_shortcode(size=size)
    return new_code


# add later 1 arg: template
def send_recovery_key(request, user, domain, message, subject, to_email):
    message = render_to_string('temmplate_recovery_page.html', {
        'user': user,
        'domain': domain,
        'message': message,
        'protocol': 'https' if request.is_secure() else 'http'
    })
    text_content = 'This is about your password recovery.'
    html_content = message
    msg = EmailMultiAlternatives(subject, text_content, 'araqelyan.aram.96@gmail.com', [to_email])
    msg.attach_alternative(html_content, "text/html")
    if msg.send():
        return True
    else:
        return False

    # old - send only str
    # email = EmailMessage(mail_subject, message, to=[to_email])
    # if email.send():
    #     return True
    # else:
    #     return False

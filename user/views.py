from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
import re
from .models import *
from django.conf import settings
from django.core.mail import EmailMessage
from django.utils import timezone
from django.urls import reverse

# Create your views here.
def SignupPage(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        passwords_have_error=False

        if User.objects.filter(username=uname).exists():
            passwords_have_error=True
            messages.error(request, "Username already exists.")
            # return render(request, 'signup.html')

        if User.objects.filter(email=email).exists():
            passwords_have_error=True
            messages.error(request, "Email already registered.")
            # return render(request, 'signup.html')
        
        # Password Match Check
        if len(password1) <= 7 :
                passwords_have_error=True
                messages.error(request, 'Password must be at least 8 characters long.')

        if password1 != password2:
            passwords_have_error=True
            messages.error(request, "Passwords do not match.")

        # Custom Validation Checks
        if not re.search(r'[A-Z]', password1):
            passwords_have_error=True
            messages.error(request, "Password must contain at least one uppercase letter.")

        if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password1):
            passwords_have_error=True
            messages.error(request, "Password must contain at least one special character.")

        


        if not passwords_have_error:
            # Create the user
            created_user = User.objects.create_user(uname, email, password1)
            created_user.save()
            # messages.success(request, "Account created successfully!")
            return redirect('signin')
        else:
            return redirect('signup')

        # # Create the user
        # created_user = User.objects.create_user(uname, email, password1)
        # created_user.save()
        # messages.success(request, "Account created successfully!")
        # return redirect('signin')

    return render(request, 'signup.html')

def Signin(request):
    if request.method == "POST":
        uname = request.POST.get('username')
        password = request.POST.get('pass')

        user = authenticate(request, username=uname, password=password)
        if user is not None:
            login(request, user)
            return redirect('upload_image')
        else:
            messages.error(request, "Invalid username or password.")
            return render(request, 'signin.html')  # Re-render with message

    return render(request, 'signin.html')

def ForgotPassword(request):
    if request.method == 'POST':
        email = request.POST.get('email')
    
        # verify if email exists
        try:
            user = User.objects.get(email=email)

            new_password_reset = PasswordReset(user=user)
            new_password_reset.save()

            password_reset_url = reverse('ResetPassword', kwargs={'reset_id': new_password_reset.reset_id})

            full_password_reset_url = f'{request.scheme}://{request.get_host()}{password_reset_url}'

            email_body = f'Reset your password using the link below:\n\n\n{full_password_reset_url}'
        
            email_message = EmailMessage(
                'Reset your password', # email subject
                email_body,
                settings.EMAIL_HOST_USER, # email sender
                [email] # email  receiver 
            )

            email_message.fail_silently = True
            email_message.send()

            return redirect('PasswordResetSent', reset_id=new_password_reset.reset_id)
        
        except User.DoesNotExist:
            messages.error(request, f"No user with email '{email}' found")
            return redirect('ForgotPassword')

        
    return render(request, 'forgot_password.html')

def PasswordResetSent(request, reset_id):

    if PasswordReset.objects.filter(reset_id=reset_id).exists():
        return render(request, 'password_reset_sent.html')
    else:
        # redirect to forgot password page if code does not exist
        messages.error(request, 'Link expired')
        return redirect('ForgotPassword')


def ResetPassword(request, reset_id):

    try:
        password_reset_id = PasswordReset.objects.get(reset_id=reset_id)

        if request.method == "POST":
            password = request.POST.get('password')
            confirm_password = request.POST.get('confirm_password')

            passwords_have_error = False

            # Password Match Check
            if password != confirm_password:
                passwords_have_error = True
                messages.error(request, "Passwords do not match.")

            # Custom Validation Checks
            if not re.search(r'[A-Z]', password):
                passwords_have_error = True
                messages.error(request, "Password must contain at least one uppercase letter.")

            if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
                passwords_have_error = True
                messages.error(request, "Password must contain at least one special character.")

            if len(password) < 8:
                passwords_have_error = True
                messages.error(request, 'Password must be at least 8 characters long.')

            expiration_time = password_reset_id.created_when + timezone.timedelta(minutes=10)

            if timezone.now() > expiration_time:
                passwords_have_error = True
                messages.error(request, 'Reset link has expired')

                password_reset_id.delete()

            if not passwords_have_error:
                user = password_reset_id.user
                user.set_password(password)
                user.save()

                password_reset_id.delete()

                messages.success(request, 'Password reset. Proceed to login')
                return redirect('signin')
            else:
                # redirect back to password reset page and display errors
                return redirect('ResetPassword', reset_id=reset_id)

    
    except PasswordReset.DoesNotExist:
        
        # redirect to forgot password page if code does not exist
        messages.error(request, 'Link Expired,')
        messages.error(request, 'Enter Email to Generate again.')
        return redirect('ForgotPassword')

    return render(request, 'reset_password.html')



def LogOut(request):
    logout(request)
    return redirect('signin')
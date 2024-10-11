from django.contrib.sites.shortcuts import get_current_site
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.template.loader import render_to_string
from django.urls import reverse_lazy, reverse
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.core.mail import EmailMultiAlternatives
from django.utils.translation import gettext_lazy as _
from django.contrib import messages

from config.settings import EMAIL_HOST_USER
from users.forms import RegistrationForm, LoginForm, ProfileUpdateForm
from users.models import CustomUserModel
from users.token import email_verification_token



def profile_view(request):
    return render(request, 'profile/profile.html')


def verify_email(request, uidb64, token):
    uid = force_str(urlsafe_base64_decode(uidb64))
    user = CustomUserModel.objects.get(pk=uid)
    if user is not None and email_verification_token.check_token(user=user, token=token):
        user.is_active = True
        user.save()
        return redirect(reverse_lazy('users:login'))
    else:
        return render(request, 'auth/email_not_verified.html')

def send_email_verification(request, user):
    token = email_verification_token.make_token(user)
    user_id = urlsafe_base64_encode(force_bytes(user.pk))
    current_site = get_current_site(request)
    verification_url = reverse('users:verify_email', kwargs={'uidb64': user_id, 'token': token})
    full_url = f"http://{current_site.domain}{verification_url}"

    text_content = render_to_string(
        'auth/verify_email.html',
        {'user': user, 'full_url': full_url}
    )

    message = EmailMultiAlternatives(
        subject='Verification Email',
        body=text_content,
        to=[user.email],
        from_email=EMAIL_HOST_USER
    )
    message.attach_alternative(text_content, 'text/html')
    message.send()


def register_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            print('salom')
            user = form.save(commit=False)
            user.set_password(raw_password=form.cleaned_data['password'])
            user.is_active = False
            user.save()
            send_email_verification(request, user)
            return HttpResponse("Email is sent to your email address.")
        else:
            errors = form.errors
            return render(request, 'auth/register/register.html', {'errors': errors})
    else:
        form = RegistrationForm()
        return render(request, 'auth/register/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect(reverse_lazy('common:success'))
            else:
                messages.error(request, _("Invalid username or password."))
    else:
        form = LoginForm()
    return render(request, 'auth/login/login.html', {'form': form})


def logout_view(request):
    logout(request=request)
    return redirect(reverse_lazy('common:home'))


def user_update_view(request):
    if request.method == 'POST':
        form = ProfileUpdateForm(instance=request.user, data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect(reverse_lazy('common:success'))
        else:
            messages.error(request, _("Invalid data."))
    else:
        form = ProfileUpdateForm()
    return render(request, 'profile/profile.html', {'form': form, 'user': request.user})

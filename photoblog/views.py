import uuid as uuid

from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import send_mail
from django.shortcuts import render, redirect

# Create your views here.


# Page Shown when not logged in
from django.template.loader import render_to_string

from photoblog.forms import RegisterForm
from photoblog.models import User


def notloggedin(request):

    return render(request, 'basics/notloggedin.html')


@login_required
def home(request):
    return render(request, 'basics/home.html')


def register(request):

    if request.method =='POST':
        form = RegisterForm(request.POST)

        if form.is_valid():

            user = form.save(commit=False)
            print("user === ? ", user)

            user.save()

            user = User.objects.get(id=user.id)
            special = user.uuid
            print(special)

            current_site = get_current_site(request)
            subject = 'Activation Link'
            message = render_to_string('auth/activation_email.html',{
                'user':user,
                'domain':current_site,
                'uuid':special,

            })
            from_email = settings.EMAIL_HOST_USER
            to_list = [user.email,settings.EMAIL_HOST_USER]
            send_mail(subject, message, from_email, to_list)

            return redirect('accountactivationsent')

        # else:
        #     return render(request, 'auth/register.html')

    form = RegisterForm()
    return render(request,'auth/register.html', {'form':form})



def accountactivationsent(request):

    print("activation sent !!!")
    return render(request, 'auth/account_activation_sent.html')


def activate(request, uuid):

    user = User.objects.get(uuid=uuid)
    #     uid = force_text(urlsafe_base64_decode(uidb64))
    #     user = User.objects.get(pk=uid)
    if user is None :
        return render(request,'auth/activation_fail.html')
    else:
        user.is_active=True
        user.email_confirm=True
        user.uuid = ''
        user.save()
        return render(request,'auth/activated.html')

import operator

from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render

from .forms import ContactForm
from .helper import get_user_on_type
from .models import Post, User


@login_required
# Create your views here.
def index(request):
    return render(request, 'website/index.html')


@login_required
def home(request):
    posts = Post.objects.order_by('-created_date')
    return render(request, 'website/pages/home.html', {'posts': posts})


@login_required
def directory(request):
    context = {}
    query = ""
    if request.GET:
        query = request.GET['q']
        context['query'] = str(query)
    brothers = sorted(get_brother_queryset(query), key=operator.attrgetter('first_name'))
    context['brothers'] = brothers
    return render(request, 'website/pages/directory.html', context)


@login_required
def save_form(form, request):
    profile = form.save(commit=False)
    user = request.user
    user.email = profile.email
    user.first_name = profile.first_name
    user.last_name = profile.last_name
    user.profile.pledge_class = profile.pledge_class
    change = False
    if not user.profile.professional_req == profile.professional_req:
        director = get_user_on_type("Professional")
        subject = "Credit Request: " + user.get_full_name()
        message = user.get_full_name() + " is requesting " + \
                  str(profile.professional_req - user.profile.professional_req) \
                  + " professional credits. " \
                    "To respond, visit the website"
        send_mail(subject, message, from_email=settings.EMAIL_HOST_USER, recipient_list=[director.email],
                  fail_silently=False)
        change = True
    if not user.profile.philanthropy_req == profile.philanthropy_req:
        director = get_user_on_type("Philanthropy")
        subject = "Credit Request: " + user.get_full_name()
        message = user.get_full_name() + " is requesting " + \
                  str(profile.philanthropy_req - user.profile.philanthropy_req) \
                  + " philanthropy credits. " \
                    "To respond, visit the website"
        send_mail(subject, message, from_email=settings.EMAIL_HOST_USER, recipient_list=[director.email],
                  fail_silently=False)
        change = True
    if not user.profile.tech_req == profile.tech_req:
        director = get_user_on_type("Tech")
        subject = "Credit Request: " + user.get_full_name()
        message = user.get_full_name() + " is requesting " + \
                  str(profile.tech_req - user.profile.tech_req) \
                  + " tech credits. " \
                    "To respond, visit the website"
        send_mail(subject, message, from_email=settings.EMAIL_HOST_USER, recipient_list=[director.email],
                  fail_silently=False)
        change = True
    if not user.profile.financial_req == profile.financial_req:
        director = get_user_on_type("Tech")
        subject = "Update Request: " + user.get_full_name()
        message = user.get_full_name() + " is requesting " + "to update his financial requirement. " \
                                                             "To update, visit the website"
        send_mail(subject, message, from_email=settings.EMAIL_HOST_USER, recipient_list=[director.email],
                  fail_silently=False)
        change = True
    user.profile.birth_date = profile.birth_date
    user.profile.img_src = profile.img_src
    user.profile.college_year_selection = profile.college_year_selection
    user.profile.image = request.FILES.get('image')
    user.profile.save()
    user.save()
    if change:
        return HttpResponse('Changes Requested')


def save_all(form, request, user):
    profile = form.save(commit=False)
    user.email = profile.email
    user.first_name = profile.first_name
    user.last_name = profile.last_name
    user.profile.image = request.FILES.get('image')
    user.profile.pledge_class = profile.pledge_class
    user.profile.financial_req = profile.financial_req
    user.profile.philanthropy_req = profile.philanthropy_req
    user.profile.tech_req = profile.tech_req
    user.profile.professional_req = profile.professional_req
    user.profile.birth_date = profile.birth_date
    user.profile.img_src = profile.img_src
    user.profile.college_year_selection = profile.college_year_selection
    user.profile.save()
    user.save()


@login_required
def account(request):
    staff = request.user.profile.is_exec()
    if request.method == 'POST':
        form = ContactForm(request.POST, request.FILES)
        if form.is_valid():
            if request.user.profile.is_exec():
                save_all(form, request)
            else:
                save_form(form, request)
    else:
        form = init_form(request.user)
    return render(request, 'website/pages/account.html', {'form': form, 'staff': staff, 'this_user': request.user})


@login_required
def brother_account(request, user_name):
    user_list = User.objects.filter(username=str(user_name))
    if len(user_list) > 0:
        user = user_list[0]
    else:
        user = None

    return render(request, 'website/pages/directory_account.html', {'this_user': user})


@login_required
def manage_account(request, user_name):
    user_list = User.objects.filter(username=str(user_name))
    if len(user_list) > 0:
        user = user_list[0]
    else:
        user = None
    if request.method == 'POST':
        form = ContactForm(request.POST, request.FILES)
        print(request.FILES)
        if form.is_valid():
            save_all(form, request, user)
    else:
        form = init_form(user)
    return render(request, 'website/pages/account.html', {'form': form, 'staff': True, 'this_user': user})



def init_form(user):
    return ContactForm(initial=
                       {'first_name': user.first_name,
                        'last_name': user.last_name,
                        'email': user.email,
                        'birth_date': user.profile.birth_date,
                        'img_src': user.profile.img_src,
                        'philanthropy_req': user.profile.philanthropy_req,
                        'professional_req': user.profile.professional_req,
                        'tech_req': user.profile.tech_req,
                        'pledge_class': user.profile.pledge_class,
                        'college_year_selection': user.profile.college_year_selection,
                        'financial_req': user.profile.financial_req,
                        'image': user.profile.image})


def get_brother_queryset(query=None):
    queryset = []
    queries = query.split(" ")
    for q in queries:
        brothers = User.objects.filter(
            Q(first_name__icontains=q) |
            Q(last_name__icontains=q)
        ).distinct()
        for brother in brothers:
            queryset.append(brother)
    return list(set(queryset))

import datetime
import operator
from random import random

from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
import django.utils.timezone
from django.utils import timezone

from rush.models import Rushee, Question, RushComment
from mysite.models import Date
from website import settings
from . import forms


# Create your views here.
def rush(request):
    form = forms.RusheeForm()
    login_form = forms.LoginForm()
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        if 'rush' in request.POST:
            # create a form instance and populate it with data from the request:
            form = forms.RusheeForm(request.POST, request.FILES)
            # check whether it's valid:
            if form.is_valid():
                # process the data in form.cleaned_data as required
                # ...
                # redirect to a new URL:
                rushee = form.save()
                rushee.random_id = int(1000 * random())
                rushee.save()
                rushee.set_username()
                rushee.save()

                subject = "Rush Application: " + rushee.first_name
                message = rushee.first_name + ", thanks for starting your rush process. Your username is " \
                          + rushee.username
                send_mail(subject, message, from_email=settings.EMAIL_HOST_USER, recipient_list=[rushee.email],
                          fail_silently=False)
                return HttpResponseRedirect('apply/' + str(rushee.username))
        elif 'login' in request.POST:
            login_form = forms.LoginForm(request.POST)
            if login_form.is_valid():
                return HttpResponseRedirect('apply/' + str(request.POST.get('username')))

    # if a GET (or any other method) we'll create a blank form
    else:
        form = forms.RusheeForm()
        login_form = forms.LoginForm()

    return render(request, 'website/rush/pages/rush_block.html', {'form': form, 'login_form': login_form})


def apply(request, username):
    questions = Question.objects.all()
    context = dict()
    context['app_open'] = Date.objects.filter(description='Application Opens')[0].date <= timezone.now() <= \
                          Date.objects.filter(description='Application Closes')[0].date
    context['app_closes'] = Date.objects.filter(description='Application Closes')[0].date
    answers = []
    if request.method == 'POST':
        rushee = Rushee.objects.filter(username=username)[0]
        questions = Question.objects.all()
        response_text = ''
        i = 0
        empty = False
        for q in questions:
            string = request.POST.get(str(i)) + ";"

            if string == ';':
                empty = True
            response_text += string
            i += 1
        rushee.responses = response_text[:-1]

        if 'apply' in request.POST:
            if empty:
                rushee.save()
                return HttpResponseRedirect('incomplete/' + str(rushee.username))
            rushee.submitted_form = True
            rushee.date_of_application = datetime.datetime.now()
            rushee.save()
            return HttpResponseRedirect('done/' + str(rushee.username))
        elif 'save' in request.POST:
            rushee.save()
            return HttpResponseRedirect('' + str(rushee.username))
    else:
        rushee = Rushee.objects.filter(username=username)[0]

        answers = rushee.responses.split(";")
        for j in range(len(questions) - len(answers)):
            answers.append('')

        dictionary = dict()
        for i in range(len(questions)):
            dictionary[questions[i]] = answers[i]

        context['rushee'] = username
        context['dict'] = dictionary
        context['dict_size'] = len(dictionary)

        return render(request, 'website/rush/pages/apply_block.html', context)


def save(request):
    return render(request, 'website/rush/pages/save_block.html', {'message': 'Save Complete'})


def done(request, username):
    return render(request, 'website/rush/pages/done_block.html', {'rushee': username})


def incomplete(request, username):
    return render(request, "website/rush/pages/incomplete_block.html", {'rushee': username})


@login_required
def directory(request):
    context = {}
    query = ""
    if request.GET:
        query = request.GET['q']
        rushees = ''
    context['query'] = str(query)
    rushees = sorted(get_rushee_queryset(query), key=operator.attrgetter('last_name'))
    context['rushees'] = rushees
    return render(request, 'website/rush/voting_directory.html', context)


def get_rushee_queryset(query=None):
    queryset = []
    queries = query.split(" ")
    for q in queries:
        rushees = Rushee.objects.filter(
            Q(first_name__icontains=q) |
            Q(last_name__icontains=q)
        ).distinct()
        for rushee in rushees:
            queryset.append(rushee)
    return list(set(queryset))


@login_required
def account(request, username):
    rushee = Rushee.objects.filter(username=username)[0]

    questions = Question.objects.all()
    answers = rushee.responses.split(";")

    for j in range(len(questions) - len(answers)):
        answers.append('')

    dictionary = dict()
    for i in range(len(questions)):
        dictionary[questions[i]] = answers[i]

    comments = rushee.comments.all()

    if request.method == 'POST':
        if 'comment_input' in request.POST:
            comment = request.POST.get('comment_input')
            created_comment = RushComment.objects.create(author=request.user, comment_text=comment, rushee=rushee)
            return HttpResponseRedirect(request.path_info)

    # This block of code allows voting (or rating) to be locked
    # voting_date = Date.objects.filter(description='Voting')
    # unlocked = False
    # if voting_date > timezone.now():
    #     unlocked = True
    return render(request, 'website/rush/account.html', {'rushee': rushee, 'dict': dictionary, 'comments': comments})


def delete(request, username, comment_id=None):
    comment = RushComment.objects.filter(id=comment_id)[0]
    comment.delete()
    return redirect('rush_account', username=username)


@login_required
def vote(request, username):
    rushee = Rushee.objects.filter(username=username)[0]
    context = dict()
    context['rushee'] = rushee
    context['is_open'] = Date.objects.filter(description='Voting')[0].date <= timezone.now()

    if request.method == 'POST':
        if 'star_1.x' in request.POST:
            rushee.aggregate_votes += 1
            rushee.num_of_votes += 1
        elif 'star_2.x' in request.POST:
            rushee.aggregate_votes += 2
            rushee.num_of_votes += 1
        elif 'star_3.x' in request.POST:
            rushee.aggregate_votes += 3
            rushee.num_of_votes += 1
        elif 'star_4.x' in request.POST:
            rushee.aggregate_votes += 4
            rushee.num_of_votes += 1
        elif 'star_5.x' in request.POST:
            rushee.aggregate_votes += 5
            rushee.num_of_votes += 1
        rushee.voters.add(request.user.profile)
        rushee.save()

    if request.user.profile in rushee.voters.all():
        context['has_voted'] = True
    else:
        context['has_voted'] = False
    return render(request, 'website/rush/vote.html', context)


def register_vote(request, username, vote_value):
    rushee = Rushee.objects.filter(username=username)[0]
    print(rushee.voters.all())
    if request.user.profile not in rushee.voters.all():
        if vote_value == 'YES':
            rushee.yes_votes += 1
        if vote_value == 'NO':
            rushee.no_votes += 1

        print(request.user.profile)
        rushee.save()
    print(rushee.voters.all())
    return redirect('rush_directory')

from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from core.models import Event
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http.response import Http404, JsonResponse

from datetime import datetime, timedelta


# Redirect user to login page
def login_user(request):
    return render(request, 'login.html')

# Proceed logout
def logout_user(request):
    logout(request) # clean session
    return redirect('/') # redirect to index page

# Form authentication
def submit_login(request):
    if request.POST: # if request is POST store 'username' and 'password' from the form
        username = request.POST.get('username')

        password = request.POST.get('password')

        # authenticate with stored login
        user = authenticate(username=username, password=password)
        if user is not None: # if user is not void proceed login and redirect to index
            login(request, user)
            #return redirect('/')
        else: # otherwise, show a message
            messages.error(request, "Invalid user or password!")
    return redirect('/') # Redirect to main page , but as it will remain in login page until it does not work

# login is required, otherwise will be kept on the same login page
@login_required(login_url='/login/')
# Function to render the HTML page
def event_list(request):
    user = request.user # store user from request
    initial_date = datetime.now() - timedelta(hours=1) #store initial date as minus one hour from now
    event = Event.objects.filter(user=user,
                                 initial_date__gt=initial_date) # Filter events for a user with initial date greater than or equal stored date
    # event = Event.objects.get(id=1) # filter one row based on id
    # event = Event.objects.all() # filter all rows
    dict = {'events':event} # dictionary
    return render(request, 'schedule.html', dict) # render created HTML template

# redirect to index
# def index(request):
#     return redirect('/schedule/')

@login_required(login_url='/login/')
def event(request):
    id_event = request.GET.get('id')
    dict = {}
    if id_event: # if id_event is not null pass it
        dict['event'] = Event.objects.get(id=id_event)
    return render(request, 'event.html', dict)

#login is required, othewise stays on the same page
@login_required(login_url='/login/')
def submit_event(request):
    if request.POST: # update attributes with the ones received from POST
        title = request.POST.get('title')
        initial_date = request.POST.get('initial_date')
        description = request.POST.get('description')
        user = request.user
        id_event = request.POST.get('id_event')
        if id_event:
            event = Event.objects.get(id=id_event)
            if event.user == user:
                event.title = title
                event.description = description
                event.initial_date = initial_date
                event.save()
            # Event.objects.filter(id=id_event).update(title=title,
                                                    #    initial_date=initial_date,
                                                    #    description=description)
        else:
            # Insert data from 'core'
            Event.objects.create(title=title,
                                initial_date=initial_date,
                                description=description,
                                user=user)
    return redirect('/')


@login_required(login_url='/login/')
def delete_event(request, id_event):
    user = request.user
    try:
        event = Event.objects.get(id=id_event) # select by received id
    except Exception:
        raise Http404()
    if user == event.user: # if event is from logged user proceeds delete
        event.delete()
    else:
        raise Http404()
    return redirect('/') # redirect to main page

@login_required(login_url='/login/')
def json_event_list(request, id_user):
    user = User.objects.get(id=id_user) # select by received id
    event = Event.objects.filter(user=user).values('id', 'title',) # select all from a user
    return JsonResponse(list(event), safe=False)
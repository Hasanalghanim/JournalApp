from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from .models import Entry
from .forms import EntryForm


def home (request):
    return render(request, 'main/home.html')


def signupuser(request):
    if request.method =="GET":
        return render(request, 'main/signupuser.html', {'form': UserCreationForm()})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('mainlogin')
            except IntegrityError:
                return render(request, 'main/signupuser.html', {'form': UserCreationForm(), 'error': 'This username has already been taken. Please select a new username.'})
        else:
            return render(request, 'main/loginuser.html', {'form': UserCreationForm(), 'error': 'Passwords did not match'})

def loginuser(request):
    if request.method == 'GET':
        return render(request, 'main/loginuser.html', {'form': AuthenticationForm()})
    else:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
                login(request, user)
                return redirect("mainlogin")

        else:
            return render(request, 'main/loginuser.html', {'form': AuthenticationForm(), 'error': 'Username and password did not match. '})

@login_required
def logoutuser(request):
    if request.method == 'POST':
        logout(request)
    return redirect('home')


@login_required
def mainlogin(request):
    entries = Entry.objects.filter(user=request.user)
    return render(request, 'main/mainlogin.html', {"entries": entries })

@login_required
def makeentry(request):
    if request.method == 'GET':
        return render(request, 'main/makeentry.html', {'form': EntryForm()})
    else:
        try:
            form = EntryForm(request.POST)
            newentry = form.save(commit=False)
            newentry.user = request.user
            newentry.save()
            return redirect('mainlogin')
        except ValueError:
            return render(request, 'main/makeentry.html', {'form': EntryForm(), 'error': 'check the fields'})


@login_required
def viewentry(request, Entry_pk):
    entry = get_object_or_404(Entry, pk=Entry_pk, user=request.user)
    entrypk = Entry_pk
    return render(request, 'main/viewentry.html', {'entry': entry, "entrypk":entrypk})





@login_required
def editentry(request, Entry_pk):
    entry = get_object_or_404(Entry, pk=Entry_pk, user=request.user)
    if request.method =="GET":
        form = EntryForm(instance=entry)
        return render(request, 'main/editentry.html', {'entry' : entry, 'form' : form})
    else:
        try:
            form = EntryForm(request.POST, instance=entry)
            form.save()
            return redirect('mainlogin')
        except ValueError:
            return render(request, 'main/editentry.html', {'entry': entry, 'form': form, 'error': 'bad information'})



@login_required
def deleteentry(request, Entry_pk):
    entry = get_object_or_404(Entry, pk=Entry_pk, user=request.user)
    if request.method == "POST":
        entry.delete()
        return redirect('mainlogin')

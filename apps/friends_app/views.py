from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .models import User

def flash_errors(errors, request):
    for error in errors:
       messages.error(request, error)

def current_user(request):
    return User.objects.get(id=request.session['user_id'])

def user(request, id):
    context={
        'user' : current_user(request),
    }
    return render(request, 'friends_app/user.html', context)

def index(request):
    return render(request, 'friends_app/index.html')

def show_user(request, userid):
    user = User.objects.get(id = userid)
    context = {
        'user': user,
        }
    return render(request, 'friends_app/users.html', context)

def register(request):
    if request.method =="POST":
        errors = User.objects.validate_registration(request.POST)

        if not errors:
            user = User.objects.create_user(request.POST)
            request.session['user_id'] = user.id
            return redirect(reverse('dashboard'))

        flash_errors(errors, request)
    return redirect(reverse('landing'))

def login(request):
    if request.method == "POST":
        check = User.objects.validate_login(request.POST)
        print check

        if 'user' in check:
            request.session['user_id'] = check['user'].id

            return redirect(reverse('dashboard'))

        flash_errors(check['errors'], request)
    return redirect(reverse('landing'))

def logout(request):
    if 'user_id' in request.session:
        request.session.pop('user_id')
    return redirect(reverse('landing'))

def friends(request):
    if 'user_id' not in request.session:
        return redirect('/')

    user = current_user(request)
    context = {
        'user': user, 
        'friends': User.objects.all()
    }
    return render(request, 'friends_app/friends.html', context)

def add_friend(request,user_id):
    user = User.objects.get(id=request.session["user_id"])
    friend = User.objects.get(id=user_id)
    user.friends.add(friend)
    return redirect('/friends')


def delete_friend(request,friend_id):
    user = User.objects.get(id=request.session["friend_id"])
    friend = Friend.objects.get(id=friend_id)
    user.friends.remove(friend)
    return redirect('/friends')
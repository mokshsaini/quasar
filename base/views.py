from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Room , Topic
from .form import RoomForm
# Create your views here.

# rooms = [
#     {'id':1,'name':'Python'},
#     {'id':2,'name':'C++'},
#     {'id':3,'name':'Java'}
# ]

def home(request):
    rooms = Room.objects.filter()
    topics = Room.objects.all()
    return render(request , "base/home.html" , {"rooms":rooms,"topics":topics})

def room(request , pk):
    # room = None
    # for i in rooms:
    #     if i["id"] == int(pk):
    #         room = i
    room = Room.objects.get(id=pk)
    return render(request , "base/room.html", {'room':room})

def createRoom(request):
    form = RoomForm()
    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    return render(request, 'base/room_form.html', {'form':form})

def updateRoom(request , pk):
    room = Room.objects.get(id=pk)
    form = RoomForm(instance=room)
    if request.method == 'POST':
        form = RoomForm(request.POST , instance=room)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request, 'base/room_form.html', {'form':form})

def deleteRoom(request , pk):
    room = Room.objects.get(id=pk)
    if request.method == 'POST':
        room.delete()
        return redirect('home')
    return render(request, 'base/delete.html', {'obj':room})

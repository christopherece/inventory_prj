from django.shortcuts import render, redirect

# Create your views here.
from pages.models import Category, Items
from queues.models import Queue
from django.db.models import Q
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.contrib import messages
from .forms import QueueForm






# Using the second database
def dashboard(request):
    hardwareCount = Queue.objects.filter(type__contains='hardware').using('dockinn_db').count()
    softwareCount = Queue.objects.filter(type__contains='software').using('dockinn_db').count()
    phoneCount = Queue.objects.filter(type__contains='phone').using('dockinn_db').count()
    accountCount = Queue.objects.filter(type__contains='other').using('dockinn_db').count()

    # queueLists = Queue.objects.filter(technician__contains = request.user.username).values() | Queue.objects.filter(technician__startswith = 'Not Assigned').values()
    # queueLists = Queue.objects.filter(Q(technician__icontains=request.user.username) | Q(technician__istartswith='Not Assigned')).values()
    queueLists = Queue.objects.using('dockinn_db').all()

    context = {
        'queueLists': queueLists,
        'hardwareCount':hardwareCount,
        'softwareCount':softwareCount,
        'phoneCount':phoneCount,
        'accountCount':accountCount,
    }
    return render(request, 'queues/queues_dashboard.html', context)


def updateticket(request, id):
    # myqueue = get_object_or_404(Queue, id=id)
    myqueue = Queue.objects.using('dockinn_db').get(id=id)
    usersList = User.objects.all()
    hardwareCount = Queue.objects.filter(type__contains='hardware').using('dockinn_db').count()
    softwareCount = Queue.objects.filter(type__contains='software').using('dockinn_db').count()
    phoneCount = Queue.objects.filter(type__contains='phone').using('dockinn_db').count()
    accountCount = Queue.objects.filter(type__contains='other').using('dockinn_db').count()


    context = {
        'myqueue':myqueue,
        'usersList':usersList,
        'hardwareCount':hardwareCount,
        'softwareCount':softwareCount,
        'phoneCount':phoneCount,
        'accountCount':accountCount,

    }
    return render(request, 'queues/updateticket.html', context)

def updatequeue(request, id):
    obj = Queue.objects.using('dockinn_db').get(id = id)
    if request.method == 'POST':
            status = request.POST['status']
            comment = request.POST['comment']
            technician = request.POST['technician']

    obj.status = status
    obj.technician = technician
    obj.comment = comment
    obj.save()
    return redirect('dashboard')

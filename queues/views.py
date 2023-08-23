from django.shortcuts import render

# Create your views here.
from pages.models import Category, Items
from .models import Queue
from django.db.models import Q



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

from django.http import JsonResponse
from django.shortcuts import render
from .models import Category, Items

# Create your views here.
def index(request):
    
    items = Items.objects.all()

    context = {
        'items':items
    }
    return render(request, 'pages/index.html', context)

def get_item_data(request):
    if request.method == 'GET':
        try:
            stock_rooms = Items.objects.values_list('stock_room', flat=True).distinct()
            stock_rooms_list = list(stock_rooms)
            return JsonResponse(stock_rooms_list, safe=False)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
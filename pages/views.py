from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from .models import Category, Items, Location
from .forms import ItemForm
from django.contrib import messages



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
        
def get_all_stockroom(request):
    locations = Location.objects.values_list('name', flat=True)  # Assuming name is the field with location names
    return JsonResponse(list(locations), safe=False)        
        
def edit_item(request, id):
    item = get_object_or_404(Items, pk=id)
    if request.method == 'POST':
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            messages.success(request, 'Item updated successfully!')
            return redirect('index')
    else:
        form = ItemForm(instance=item)
    context = {'form': form}
    return render(request, 'pages/index.html', context)
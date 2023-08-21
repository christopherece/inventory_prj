from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from .models import Category, Items
from .forms import ItemForm

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
        
def edit_item(request, id):
    items = get_object_or_404(Items, pk=id)
    if request.method == 'POST':
        form = ItemForm(request.POST, instance=items)
        if form.is_valid():
            form.save()
            context = {
                 'success': True,
                 'success_message': 'Feedback saved successfully!',
                 'success_image': '/static/img/thumbsup.gif',
                 'success_class': 'alert alert-success',
                 
             }
            return redirect('index')
    else:
        form = ItemForm(instance=items)
    context = {'form':form}
    return render(request, 'pages/index.html', context)
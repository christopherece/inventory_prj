from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from .models import Category, Items, Location
from users.models import Profile
from .forms import ItemForm
from django.contrib import messages
from django.contrib.auth.models import User



# Create your views here.
def index(request):
    
    items = Items.objects.all()
    context = {
        'items':items
    }
    print(items)
    return render(request, 'pages/index.html', context)

def get_item_data(request):
    if request.method == 'GET':
        try:
            locations = Items.objects.values_list('location', flat=True).distinct()
            locations_list = list(locations)
            return JsonResponse(locations_list, safe=False)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
        
def get_all_stockroom(request):
    locations = Location.objects.values('id', 'name')  # Fetch both ID and name
    return JsonResponse(list(locations), safe=False)        
        

def get_user_info(request):
    if request.method == 'GET':
        username = request.GET.get('username')  # Assuming the parameter is named 'userId'
        user = get_object_or_404(User, username=username)  # Replace with your actual User model

        # Create a dictionary with user information
        user_info = {
            'id': user.id,
            'username': user.username,
            'email': user.email,
            # Add more fields as needed
        }

        return JsonResponse(user_info)
    else:
        return JsonResponse({'error': 'Invalid request method'})
    
def get_all_users(request):
    users = Profile.objects.values_list('fname', flat=True)  # Assuming name is the field with location names
    return JsonResponse(list(users), safe=False)        
        
def edit_item(request, id):
    obj = get_object_or_404(Items, id=id)  # Use get_object_or_404 to handle not found cases
    
    if request.method == 'POST':
        notes = request.POST['notes']
        allocated_to = request.POST['allocated_to']

        location_id = request.POST['location']  # Assuming the location_id is sent from the form
        
        location_instance = get_object_or_404(Location, id=location_id)  # Get the Location instance
        
        obj.notes = notes
        obj.allocated_to = allocated_to

        obj.location = location_instance  # Assign the Location instance
        obj.save()
        
        return redirect('index')
    
    # Handle the case when the request method is not POST (optional)
    
    return render(request, 'index.html', {'obj': obj})

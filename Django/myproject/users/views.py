from django.shortcuts import render
from .models import Profile

def profiles(request):
    # Assuming you want to display the profile of the first user in the database
    profile = Profile.objects.first()

    # If you have a specific user in mind, you can filter accordingly, e.g., Profile.objects.get(user=some_user)
    
    return render(request, 'users/profiles.html', {'profile': profile})

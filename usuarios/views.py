from django.shortcuts import render
from .models import Profile
# Create your views here.
def index(request):
    profiles = Profile.objects.all()
    context = {
        "profiles":profiles,
        
    }
    return render(request,"index.html",context)
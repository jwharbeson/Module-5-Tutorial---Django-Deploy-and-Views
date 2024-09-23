from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone

# View that shows current time
def current_time(request):
    now = timezone.now()
    return HttpResponse(f"Current time is: {now}")

# View to display homepage
def home(request):
    return render(request, 'home.html')

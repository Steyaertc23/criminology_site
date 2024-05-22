from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Criminal

# Create your views here.
@login_required(login_url='/login')
def home(request):
    return render(request, 'crimdb/home.html')

@login_required(login_url='/login')
def search(request, name):
    # case insensitive
    criminals = Criminal.objects.filter(full_name__icontains=name)

    return render(request, 'crimdb/search.html', {criminals})
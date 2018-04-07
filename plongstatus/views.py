from django.shortcuts import render

# Create your views here.
from .models import Status

def status(request):
    """
    View function for homepage of site
    """
    current_status = Status.objects.get(pk=1)

    return render(
        request,
        'status.html',
        context={'current_status':current_status},
    )

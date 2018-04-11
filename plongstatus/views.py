from django.shortcuts import render

# Create your views here.
from .models import Status
from datetime import datetime
import sqlite3

def status(request):
    """
    View function for homepage of site
    """

    current_status = Status.objects.last()

    return render(
        request,
        'status.html',
        context={'current_status':current_status.status, 'timestamp':current_status.timestamp},
    )

from django.views.decorators.csrf import csrf_exempt
from .forms import UpdateStatus
from .models import models

@csrf_exempt
def updatestatus(request):
    """
    If form is submitted.
    """
    if request.method == 'POST':
        form = UpdateStatus(request.POST)

        if form.is_valid():
            current_time = datetime.now()
            current_status = Status(status=form.cleaned_data['status'], timestamp=current_time)
            current_status.save()

            return render(
                request,
                'updated.html',
                context={'status':form.cleaned_data['status'],'timestamp':current_time}
            )

        else:
            return render(
                request,
                'updateerror.html',
                context={'form.errors':form.errors, 'form.non_field_errors':form.non_field_errors}
            )

    else:
        #Handle a GET request or anything else. TODO: finish this section later.
        return render(
            request,
            'updateerror.html',
        )

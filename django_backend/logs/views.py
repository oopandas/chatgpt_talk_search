from django.shortcuts import render
from django.http import HttpResponse
from .models import ChatLogModel

def index(request):
    logs = ChatLogModel.objects.all()

    context = {
        "logs": logs
    }
    return render(request, "logs/index.html", context)
# Create your views here.

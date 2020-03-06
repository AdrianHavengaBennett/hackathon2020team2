from django.shortcuts import render
from .models import User


# Create your views here.
def get_user_details(request):
    users = User.objects.all()
    return render(request, "index.html", {"users": users})


def add_new_user(request):
    pass

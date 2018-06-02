from django.shortcuts import render, HttpResponse, redirect
from django.core import serializers
import json
from django.contrib import messages
from apps.posts.models import *


# Create your views here.
def index(request):
    records = Post.objects.all().order_by("-created_at")

    context = {
        "records": records
    }

    return render(request, "posts/index.html", context)


def post(request):
    if request.method == "POST":
        errors = Post.objects.record_validator(request.POST)
        if len(errors):
            for key, value in errors.items():
                messages.error(request, value)
        else:
            Post.objects.create(note = request.POST["note"])
            records = Post.objects.all().order_by("-created_at")
            return HttpResponse(serializers.serialize("json", records), content_type = 'application/json')

    return redirect("/posts/index")

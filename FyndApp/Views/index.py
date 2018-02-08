from django.shortcuts import HttpResponse, render, get_object_or_404

def dashboard(request):
    return render(request,'index.html',{})
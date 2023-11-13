from django.shortcuts import render

def home(request):
    return render(request,'principalPage/index/index.html')

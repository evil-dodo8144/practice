from django.shortcuts import render

# Create your views here.
def all_dodo(request):
    return render(request,'dodoapp/dodoapp.html')
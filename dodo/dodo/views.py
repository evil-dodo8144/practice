"""date- 11/01/2026
this is views page .
def--
    This file takes request from urls.py and send it to model.py and look into database and then 
    take response from them and send it to user as "response" """
from django.http import HttpResponse
from django.shortcuts import render
"""rendering html file through django shortcut"""
def home(request):
    #return HttpResponse("it is a method of returning a response by using function request")
    return render(request, 'website/index.html')

def about(request):
    # return HttpResponse("it is about page")
    """this is the rendering process to push our stule.css
    for about page by rendering our index.html files 
    from templates"""
    return render(request, 'website/index1.html')
def contact(request):
    #return HttpResponse("it is contact page")
    return render(request,'website/index_contact.html')
from django.shortcuts import render

# Create your views here.

def index(request):
    context_dict = {'text':'Hello World!','number':100}
    return render(request,'basicapp/Index.html',context_dict)

def other(request):
    return render(request,'basicapp/Other.html')

def relative(request):
    return render(request,'basicapp/Relative.html')

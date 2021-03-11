from django.shortcuts import render

# Create your views here.
def index(request):
    context_dict={'text':'Hello world!','number':100}
    return  render(request,'basic_app/index.html', context_dict)

def other(request):
    return render(request,'basic_app/other.html')

def relative(request):
    return render(request,'basic_app/relative_url_templates.html')

def index2(request):
    context_dict={'text':'Test Template!','number':100}
    return render(request,'basic_app/index2.html', context_dict)

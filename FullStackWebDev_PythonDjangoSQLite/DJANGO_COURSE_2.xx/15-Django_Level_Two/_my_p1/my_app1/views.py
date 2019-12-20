from django.shortcuts import render

# Create your views here.
def index(request):
    my_dict = {'insert_content': "HELLO IM FROM APP1!"}
    return render(request,'my_app1/index.html',context=my_dict)

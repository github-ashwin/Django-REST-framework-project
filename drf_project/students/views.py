from django.shortcuts import render,HttpResponse

# Create your views here.
def students(request):
    student = [
        {
            'id':1,
            'name':"John Doe",
            'age':20
        }
    ]
    return HttpResponse(student)
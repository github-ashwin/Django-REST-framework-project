from django.shortcuts import render
from django.http import JsonResponse
from students.models import Student
from .serializers import StudentSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

# Create your views here.

# def studentsView(request):
#     student = Student.objects.all()
#     # Manual Serialization - only in simple usecases, not suitable for complex data
#     # student_list = list(student.values())

#     return JsonResponse(student_list,safe=False) # safe = False determines we are not passing dictionary values but it is safe

# Function based view
@api_view(['GET','POST'])
def studentsView(request):
    if request.method == 'GET':
        student = Student.objects.all()
        serializer = StudentSerializer(student, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            print(serializer.errors)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

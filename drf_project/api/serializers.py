from rest_framework import serializers
from students.models import Student
from employee.models import Employee

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = "__all__"

class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField(max_length=255)
    overview = serializers.CharField()
    release_date = serializers.DateField()
    poster_path = serializers.CharField()
    popularity = serializers.FloatField()
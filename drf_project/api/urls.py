from django.urls import path
from . import views
from tmdb_sample.views import PopularMoviesView
urlpatterns = [
    path('students/',views.studentsView),
    path('students/<int:pk>/',views.studentDetailView),
    path('employees/',views.Employees.as_view()), # For class based views, as_view() is necessary
    path('employees/<int:pk>/',views.EmployeeDetails.as_view()),
    path('popular/', PopularMoviesView.as_view())
]

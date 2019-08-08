from django.urls import path
from . import views
from django.views import View

urlpatterns = [
    path('', views.index, name='index'),
    path('flights/list/', views.ListFlightListView.as_view(), name='flights-list'),
    path('flights/create/', views.CreateFlightCreateView.as_view()),
    path('flights/update/<int:pk>/', views.UpdateFlightUpdateView.as_view()),
    path('flights/<int:pk>/', views.DetailFlightDetailView.as_view()),
    path('flights/delete/<int:pk>/', views.DeleteFlightDeleteView.as_view()),
    path('login/', views.UserLoginView.as_view()),
]
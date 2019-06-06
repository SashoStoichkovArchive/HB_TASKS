from django.urls import path
from . import views
from django.views import View

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:plane_id>/', views.details, name='plane'),
    path('flights/', views.flights, name='flights'),
    path('flights/list/', views.ListFlightListView.as_view(), name='flights-list'),
    path('flights/create/', views.create_flight),
    path('flights/create-from-class-view/', views.CreateFlightView.as_view()),
    path('flights/create-from-create-view/', views.CreateFlightCreateView.as_view()),
    path('flights/update-from-update-view/<int:pk>/', views.UpdateFlightUpdateView.as_view()),
    path('flights/<int:pk>/', views.DetailFlightDetailView.as_view()),
    path('flights/delete/<int:pk>/', views.DeleteFlightDeleteView.as_view()),
    path('login/', views.UserLoginView.as_view()),
]
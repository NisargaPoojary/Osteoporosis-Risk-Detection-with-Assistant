from django.urls import path
from . import views

urlpatterns = [
    path('predict_osteoporosis', views.predict_osteoporosis, name='predict_osteoporosis'),
    path('bmi_calculator/', views.bmi_calculator, name='bmi_calculator'),
]

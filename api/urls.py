from django.urls import path
from api import views

urlpatterns = [
    path('brands/<str:brand_id>/', views.get_recommendations, name='get_recommendations'),

]
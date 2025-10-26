from django.urls import path
from my_app import views

urlpatterns = [
    path('',views.fun1,name="homec"),
    path('first/',views.fun2,name="firstc"),
    path('second/',views.fun3,name="secondc"),
    path('analysis/',views.analyze_review,name="senti_analysis")
]

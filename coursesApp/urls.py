from django.urls import path     
from . import views
urlpatterns = [
    path('', views.index),	   
    path("add_course",views.add_course),
    path("delete_course/<int:id>",views.delete_course),
    path('remove/<int:id>',views.remove)
]
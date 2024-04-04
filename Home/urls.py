
from django.urls import path  
from . import views

urlpatterns = [
    path ('',views.index, name='index'),
    # path('About/',views.months),
    path('add_student/',views.add_student),
    path('add_parent/',views.add_parent),
    
    path('update/<int:id>/',views.update_student, name='update'),
    path('retrieve_student/<int:id>/',views.retrieve_student,),
    path ('delete/<int:id>/',views.delete_student, name ='delete')
    
]
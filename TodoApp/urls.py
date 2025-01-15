from django.urls import path
from TodoApp import views
urlpatterns = [
    
    path('',views.home,name='home'),
    
    path('todolist/',views.todolist,name='todolist'),
    
    path('todolist/delete/<task_id>',views.delete,name='delete'),
    
    path('todolist/edit/<task_id>',views.edit_task,name='edit_task'),
    
    path('todolist/mark_done/<task_id>',views.mark_done,name='mark_done'),
    
    path('todolist/mark_pending/<task_id>',views.mark_pending,name='mark_pending'),
]

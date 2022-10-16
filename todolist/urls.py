from django.urls import path
from todolist.views import delete_task_ajax, register, login_user, logout_user, show_json, show_todolist, create_task, delete_task, update_task, delete_task_ajax, add_task_ajax, update_task_ajax, show_json

app_name = 'todolist'

urlpatterns = [
    path('', show_todolist, name='show_todolist'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('create-task/', create_task, name='create-task'),
    path('<id>/delete/', delete_task, name='delete-task'),
    path('<id>/update/', update_task, name='update-task'),
    path('json/', show_json, name='show_json'),
    path('delete/<id>', delete_task_ajax, name='delete-task-ajax'),
    path('add/', add_task_ajax, name='create-task-ajax'),
    path('update/<id>', update_task_ajax, name='update-task-ajax'),
]
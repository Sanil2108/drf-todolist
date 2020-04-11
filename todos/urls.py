from django.urls import path
from todos.views import TodoListUpdateView, TodoItemView, TodoListDetailView

urlpatterns = [
    path('todo_list/', TodoListUpdateView.as_view(), name = 'TODO List update view'),
    path('todo_list/<int:todolist_id>/', TodoListDetailView.as_view(), name = 'TODO List Detail view'),
    path('todo_item/<int:todolist_id>/', TodoItemView.as_view(), name = 'TODO List item'),
]
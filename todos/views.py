from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from users.models import User, Token
from users.serializers import UserDetailSerializer, UserRetrievalSerializer, TokenSerializer, UserPasswordAuthenticationSerializer

from todos.serializers import TodoListSerializer, TodoItemSerializer
from todos.models import TodoList, TodoItem

class TodoListUpdateView(APIView):
    def post(self, request):
        if 'user' not in request.data:
            return Response(status = status.HTTP_401_UNAUTHORIZED)

        userData = request.data['user']
        userRetrievalSerializer = UserRetrievalSerializer(data = userData)
        userRetrievalSerializer.is_valid(raise_exception = True)
        user = userRetrievalSerializer.create()

        if 'token' not in request.data.keys():
            return Response(status = status.HTTP_401_UNAUTHORIZED)

        tokenData = request.data['token']
        tokenSerializer = TokenSerializer(data = tokenData)
        tokenSerializer.is_valid(raise_exception = True)
        token = tokenSerializer.create()
        
        if not user.is_token_valid(token):
            return Response(status = status.HTTP_401_UNAUTHORIZED)
        
        if 'todoList' not in request.data:
            return Response(status = status.HTTP_400_BAD_REQUEST)

        todoListSerializer = TodoListSerializer(data = request.data['todoList'])
        todoListSerializer.is_valid(raise_exception = True)
        todoList = todoListSerializer.create()
        todoList.owner = user
        todoList.save()

        return Response(status = status.HTTP_200_OK)

    def delete(self, request):
        pass

class TodoListDetailView(APIView):
    def post(self, request, todolist_id):
        todoList = TodoList.objects.all().get(pk = todolist_id)
        if todoList.private:
            if 'user' not in request.data:
                return Response(status = status.HTTP_401_UNAUTHORIZED)

            userData = request.data['user']
            userRetrievalSerializer = UserRetrievalSerializer(data = userData)
            userRetrievalSerializer.is_valid(raise_exception = True)
            user = userRetrievalSerializer.create()

            if 'token' not in request.data.keys():
                return Response(status = status.HTTP_401_UNAUTHORIZED)

            tokenData = request.data['token']
            tokenSerializer = TokenSerializer(data = tokenData)
            tokenSerializer.is_valid(raise_exception = True)
            token = tokenSerializer.create()
            
            if user == todoList.owner:
                return Response(TodoListSerializer(todoList).data, status = status.HTTP_200_OK)
            else:
                return Response(status = status.HTTP_401_UNAUTHORIZED)
        else:
            return Response(TodoListSerializer(todoList).data, status = status.HTTP_200_OK)

class TodoItemView(APIView):
    def post(self, request, todolist_id):
        todoList = TodoList.objects.all().get(pk = todolist_id)
        if 'user' not in request.data:
            return Response(status = status.HTTP_401_UNAUTHORIZED)

        userData = request.data['user']
        userRetrievalSerializer = UserRetrievalSerializer(data = userData)
        userRetrievalSerializer.is_valid(raise_exception = True)
        user = userRetrievalSerializer.create()

        if 'token' not in request.data.keys():
            return Response(status = status.HTTP_401_UNAUTHORIZED)

        tokenData = request.data['token']
        tokenSerializer = TokenSerializer(data = tokenData)
        tokenSerializer.is_valid(raise_exception = True)
        token = tokenSerializer.create()
        
        if user == todoList.owner:
            todoItemSerializer = TodoItemSerializer(data = request.data['todo_item'])
            todoItemSerializer.is_valid(raise_exception = True)
            todoItem = todoItemSerializer.create()

            todoItem.todoList = todoList
            todoItem.save()

            return Response(status = status.HTTP_200_OK)
        
        return Response(status = status.HTTP_401_UNAUTHORIZED)
            

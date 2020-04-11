from rest_framework import serializers
from todos.models import TodoList, TodoItem
from users.models import User


class TodoItemSerializer(serializers.ModelSerializer):
    def create(self, validated_data = None):
        if validated_data == None:
            validated_data = self.validated_data
        return TodoItem(**validated_data)

    class Meta():
        model = TodoItem
        fields = ['name', 'description']


class TodoListSerializer(serializers.ModelSerializer):
    owner = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), required = False)
    todoitem_set = TodoItemSerializer(many=True)

    def create(self, validated_data = None):
        if validated_data == None:
            validated_data = self.validated_data
        return TodoList(**validated_data)

    class Meta():
        model = TodoList
        fields = ['owner', 'title', 'private', 'todoitem_set']

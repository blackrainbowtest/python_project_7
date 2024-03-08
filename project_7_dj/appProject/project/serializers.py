from rest_framework.serializers import ModelSerializer
from django.contrib.auth.models import User
from .models import Task, Categories, Creater


class UserSerializers(ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'username', 'email', 'is_superuser']


class DeveloperSerializers(ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']


class CategorySerializers(ModelSerializer):
    class Meta:
        model = Categories
        fields = ['id', 'name']


class CreaterSerializers(ModelSerializer):
    user = UserSerializers()

    class Meta:
        model = Creater
        fields = ['id', 'user', 'description']


class TasksSerializers(ModelSerializer):
    categories = CategorySerializers()
    assigned_to = UserSerializers()
    created_by = CreaterSerializers()

    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'categories', 'assigned_to', 'created_by']

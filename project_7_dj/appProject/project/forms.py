from django.contrib.auth.models import User
from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import UserCreationForm, SetPasswordForm
from .models import Task, Categories, Creater, FailedLogins, PasswordRecovery


class UserForm(UserCreationForm):
    first_name = forms.CharField(min_length=3, max_length=32)
    last_name = forms.CharField(min_length=3, max_length=32)
    username = forms.CharField(min_length=5, max_length=16)
    email = forms.CharField(min_length=5, max_length=56)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'password1', 'password2', 'email')


class CategoriesForm(ModelForm):

    class Meta:
        model = Categories
        fields = ('name', )


class CreaterForm(ModelForm):
    description = forms.CharField(required=False, empty_value=None)

    class Meta:
        model = Creater
        fields = ('user', 'description')


class TasksForm(ModelForm):
    description = forms.CharField(required=False, empty_value=None)
    assigned_to = forms.CharField(required=False, empty_value=None)

    class Meta:
        model = Task
        fields = ('title', 'description', 'categories', 'created_by', 'assigned_to')


class FailedLoginsForm(ModelForm):
    class Meta:
        model = FailedLogins
        fields = ('user', 'time_stamp', 'count')


class PasswordRecoveryForm(ModelForm):
    class Meta:
        model = PasswordRecovery
        fields = ('user', 'shortcode', 'updated')


class SetPasswordForm(SetPasswordForm):
    class Meta:
        model = User
        fields = ('new_password1', 'new_password2')

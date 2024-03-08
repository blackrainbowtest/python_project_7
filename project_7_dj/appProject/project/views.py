from django.shortcuts import render
from django.http import HttpResponseNotFound
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response

from django.contrib.auth import authenticate, logout
from rest_framework.authtoken.models import Token

from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User

# Data connection
from .forms import UserForm, CreaterForm, TasksForm, CategoriesForm, FailedLoginsForm, SetPasswordForm, \
    PasswordRecoveryForm
from .serializers import UserSerializers, TasksSerializers, CategorySerializers, DeveloperSerializers
from .models import Task, Categories, Creater, FailedLogins, PasswordRecovery

# template to string for email
from django.template.loader import render_to_string
    # from django.contrib.sites.shortcuts import get_current_site
    # from django.utils.encoding import force_bytes, force_str
# email send
from django.core.mail import EmailMessage

# datetime
from time import gmtime, strftime
from datetime import datetime, timedelta
import pytz

# update method a + 1
from django.db.models import F

# required check
# from django.contrib.auth.decorators import login_required
from .utils import update_shortcode, send_recovery_key

# password change
from django.contrib.auth.forms import PasswordChangeForm, SetPasswordForm

# User SignUp/SignIn

@api_view(['POST'])
def signup(request):
    if request.method == 'POST':
        form = UserForm(request.data)
        if form.is_valid():
            form.save()
            return Response({'data': 'Success'})
        else:
            return Response({'errors': form.errors})
    return HttpResponseNotFound("Wrong request method. Try again.")


@api_view(['POST'])
def signin(request):
    if request.method == 'POST':
        username = request.data.get('username')
        password = request.data.get('password')
        if username is None or password is None:
            return Response({'errors': ['Please enter all Fields']})
        userTest = User.objects.filter(username=username)
        if len(userTest) > 0:
            user = authenticate(username=username, password=password)
            isFail = FailedLogins.objects.filter(user=userTest[0])
            if user is None:
                showtime = strftime("%Y-%m-%d %H:%M:%S", gmtime())
                failForm = ''
                # when reong password
                if len(isFail) > 0:
                    lastFailDateTime = isFail[0].time_stamp
                    currentDateTime = datetime.strptime(showtime, "%Y-%m-%d %H:%M:%S") - timedelta(minutes = 1)
                    if lastFailDateTime.replace(tzinfo=None) < currentDateTime.replace(tzinfo=None):
                        # delete old if more than 5 minutes
                        FailedLogins.objects.get(pk=isFail[0].id).delete()
                        # set new fail
                        failForm = FailedLoginsForm({'user': userTest[0].id, 'time_stamp': showtime, 'count': 1})
                        if failForm.is_valid():
                            failForm.save()
                    else:
                        if isFail[0].count < 3:
                            FailedLogins.objects.filter(pk=isFail[0].id).update(count= F("count") + 1)
                        else:
                            temp = timedelta(minutes = 1) - (datetime.strptime(showtime, "%Y-%m-%d %H:%M:%S").replace(tzinfo=None) \
                                   - lastFailDateTime.replace(tzinfo=None))
                            return Response({'errors': {'username': [f'The account was banned.'],
                                                        'countDown': temp}})
                else:
                    # if no fail in base add new one
                    failForm = FailedLoginsForm({'user':userTest[0].id, 'time_stamp': showtime, 'count': 1})
                    if failForm.is_valid():
                        failForm = failForm.save()
                isFail = FailedLogins.objects.filter(user=userTest[0])
                return Response({'errors': {'username': [f'Wrong login or password. {4 - isFail[0].count} tries left']}})
            else:
                if len(isFail) > 0:
                    showtime = strftime("%Y-%m-%d %H:%M:%S", gmtime())
                    lastFailDateTime = isFail[0].time_stamp
                    currentDateTime = datetime.strptime(showtime, "%Y-%m-%d %H:%M:%S") - timedelta(minutes = 1)
                    if lastFailDateTime.replace(tzinfo=None) < currentDateTime.replace(tzinfo=None):
                        FailedLogins.objects.get(pk=isFail[0].id).delete()
                    else:
                        if isFail[0].count >= 3:
                            # add if count < 3 than all norm
                            temp = timedelta(minutes = 1) - (
                                        datetime.strptime(showtime, "%Y-%m-%d %H:%M:%S").replace(tzinfo=None) \
                                        - lastFailDateTime.replace(tzinfo=None))
                            return Response({'errors': {'username': [f'Your account is blocked.'],
                                                        'countDown': temp}})
                        else:
                            FailedLogins.objects.get(pk=isFail[0].id).delete()
                # token = key, , _ boolean val
                token, _ = Token.objects.get_or_create(user=user)
                return Response({'token': token.key})
        else:
            return Response({'errors': {'username': ['Wrong username.']}})
    return HttpResponseNotFound("Wrong request method. Try again.")


# user auth
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def profile(request):
    user = UserSerializers(request.user).data
    return Response({'data': user})


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def userLogout(request):
    request.user.auth_token.delete()  # delete from DB
    logout(request)  # logout from session
    return Response({'msg': 'OK'})

# User SignUp/SignIn


# ToDos
# GET
@api_view(['GET'])
def getCategorys(request):
    if request.method == 'GET':
        pass
    return HttpResponseNotFound("Wrong request method. Try again.")


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def addCategory(request):
    if request.method == 'POST':
        pass
    return HttpResponseNotFound("Wrong request method. Try again.")


@api_view(['GET'])
def getTasks(request, value):
    if request.method == 'GET':
        tasksAPI = Task.objects.filter(categories=value)
        categoryName = Categories.objects.get(pk=value).name
        return Response({'data': TasksSerializers(tasksAPI, many=True).data,
                         'category': categoryName})
    return HttpResponseNotFound("Wrong request method. Try again.")


@api_view(['GET'])
def getCategories(request):
    if request.method == 'GET':
        categoriesAPI = Categories.objects.all()[1:]
        return Response({'data': CategorySerializers(categoriesAPI, many=True).data})
    return HttpResponseNotFound("Wrong request method. Try again.")


@api_view(['GET'])
def getArchive(request, value):
    if request.method == 'GET':
        tasksAPI = Task.objects.filter(categories=value)
        categoryName = Categories.objects.get(pk=value).name
        return Response({'data': TasksSerializers(tasksAPI, many=True).data,
                         'category': categoryName})
    return HttpResponseNotFound("Wrong request method. Try again.")


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getDevelopers(request):
    if request.method == 'GET':
        usersAPI = User.objects.exclude(pk=request.user.id).exclude(is_superuser=True)
        return Response({'data': DeveloperSerializers(usersAPI, many=True).data})
    return HttpResponseNotFound("Wrong request method. Try again.")


# POST -----------------------------------------------------------------------------------------------------------------
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def addTask(request):
    if request.method == 'POST':
        createrData = CreaterForm({'user': request.user.id})
        if createrData.is_valid():
            created_by = createrData.save()
            request.data['created_by'] = created_by.id
            taskAPI = TasksForm(request.data)
            if taskAPI.is_valid():
                taskAPI.save()
                tasksAPI = Task.objects.filter(categories=request.data['categories'])
                return Response({'data': TasksSerializers(tasksAPI, many=True).data})
            else:
                return Response({'errors': taskAPI.errors})
    return HttpResponseNotFound("Wrong request method. Try again.")


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def sendInvite(request):
    if request.method == 'POST':
        mail_subject = 'Invite.'
        message = render_to_string('template_Invite_page.html', {
            'user': request.user.username,
            'domain': 'http://localhost:8080?invite=true',
            'message': request.data['message'],
            'protocol': 'https' if request.is_secure() else 'http'
        })
        email = EmailMessage(mail_subject, message, to=[request.data['email']])
        if email.send():
            return Response({'data': 'Invite sent successfully.'})
        else:
            return Response({'errors': 'An unexpected error occurred. When Check your details.'})
    return HttpResponseNotFound("Wrong request method. Try again.")


@api_view(['POST'])
def recoveryPassword(request):
    if request.method == 'POST':
        user_exists = User.objects.filter(username=request.data['username']).exists()  # check is user exists
        if user_exists:  # if user is exists than
            user = User.objects.get(username=request.data['username']).id  # get user id
            updateData = {'user': user, 'updated': datetime.now().replace(tzinfo=None)}
            prDB = PasswordRecoveryForm(updateData)  # send data to form
            if prDB.is_valid():  # if form is valid
                pr_exists = PasswordRecovery.objects.filter(user=user).exists()  # check is user allready send message?
                if pr_exists:
                    pr_get = PasswordRecovery.objects.get(user=user)
                    dateTimeNow = datetime.now().replace(tzinfo=None) - timedelta(minutes=2)  # check time less
                    if pr_get.updated.replace(tzinfo=None) < dateTimeNow:  # minutes passed
                        PasswordRecovery.objects.filter(pk=pr_get.id).update(updated=datetime.now().replace(tzinfo=None),
                            shortcode=update_shortcode(PasswordRecovery))
                        shortcode = PasswordRecovery.objects.get(pk=pr_get.id).shortcode
                        # SEND MAIL ------------------------------------------------------------------------------------
                        send_recovery_key(request, User.objects.get(pk=user).username,
                        f'http://localhost:8080?username={User.objects.get(pk=user).username}&shortcode={shortcode}',
                        shortcode, 'Password recovery', User.objects.get(pk=user).email)
                        return Response({'data': 'New message sent successfully. Check your email.'})
                    else:  # not passed w8 some time
                        return Response({'data': 'You have already submitted a request. Check your email.'})
                else:
                    pr_get = prDB.save()
                    shortcode = PasswordRecovery.objects.get(pk=pr_get.id).shortcode
                    # SEND MAIL ----------------------------------------------------------------------------------------
                    send_recovery_key(request, User.objects.get(pk=user).username,
                    f'http://localhost:8080?username={User.objects.get(pk=user).username}&shortcode={shortcode}',
                    shortcode, 'Password recovery', User.objects.get(pk=user).email)
                    return Response({'data': 'Password recovery sent successfully. Check your email.'})
            else:  # impossible but reinsurance would not hurt
                print(prDB.errors)
            return Response({'data': 'Password recovery sent successfully. Check your email.'})
        else:  # else if user is not exists than
            return Response({'data': 'Unknown user. Check your username and try again.'})
    return HttpResponseNotFound("Wrong request method. Try again.")


@api_view(['POST'])
def passwordChange(request):
    if request.method == 'POST':
        shortcode = request.data['shortcode']
        del request.data['shortcode']
        userName = request.data['username']
        del request.data['username']
        user_exists = User.objects.filter(username=userName).exists()
        if user_exists:  # if user is exists
            user = User.objects.get(username=userName)
            shortcode_exists = PasswordRecovery.objects.filter(shortcode=shortcode, user=user).exists()
            if shortcode_exists:  # if shortcode is exists
                shortcode = PasswordRecovery.objects.get(shortcode=shortcode, user=user)
                form = SetPasswordForm(user, request.data)
                if form.is_valid():
                    user = form.save()
                    shortcode.delete()
                    return Response({'data': 'Password changed success.'})
                else:
                    return Response({'errors': form.errors})
            else:
                return Response({'errors': {'new_password1': ['Unknown callback. Send password request again.']}})
        else:
            return Response({'errors': {'new_password1': ['Unknown user. Check your username and try again.']}})
        return Response({'data': 'Password recovery sent successfully. Check your email.'})
    return HttpResponseNotFound("Wrong request method. Try again.")


# Update ---------------------------------------------------------------------------------------------------------------
@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def updateTask(request):
    if request.method == 'PUT':
        taskID = request.data['id']
        del request.data['id']
        Task.objects.filter(pk=taskID).update(**request.data)
        tasksAPI = Task.objects.filter(categories=request.data['categories'])
        categoryName = Categories.objects.get(pk=request.data['categories']).name
        return Response({'data': TasksSerializers(tasksAPI, many=True).data,
                         'category': categoryName})
    return HttpResponseNotFound("Wrong request method. Try again.")


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def updateDescription(request):
    if request.method == 'PUT':
        taskID = request.data['id']
        del request.data['id']
        if request.user.id == Task.objects.get(pk=taskID).created_by.user.id:
            Task.objects.filter(pk=taskID).update(**request.data)
        tasksAPI = Task.objects.filter(categories=request.data['categories'])
        categoryName = Categories.objects.get(pk=request.data['categories']).name
        return Response({'data': TasksSerializers(tasksAPI, many=True).data,
                         'category': categoryName})
    return HttpResponseNotFound("Wrong request method. Try again.")


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def updateDraggable(request):
    if request.method == 'PUT':
        tasksID = request.data['tasks']
        del request.data['tasks']
        Task.objects.filter(pk__in=tasksID).update(**request.data)
        tasksAPI = Task.objects.filter(categories=request.data['categories'])
        categoryName = Categories.objects.get(pk=request.data['categories']).name
        return Response({'data': TasksSerializers(tasksAPI, many=True).data,
                         'category': categoryName})
    return HttpResponseNotFound("Wrong request method. Try again.")


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def updateAssigned(request):
    if request.method == 'PUT':
        tasksID = request.data['task']
        creatorDescription = request.data['description']
        del request.data['task']
        del request.data['description']
        if request.data['categories'] == 2 or request.data['categories'] == 3:
            createdID = Task.objects.filter(pk=tasksID)[0].created_by.id
            Creater.objects.filter(pk=createdID).update(description=creatorDescription)
            Task.objects.filter(pk=tasksID).update(**request.data)

            mail_subject = 'Assigned task.'
            message = render_to_string('template_Assigned_page.html', {
                'user': request.user.username,
                'domain': 'http://localhost:8080/todos',
                'message': 'You have been assigned a new task. Check your tasks.',
                'protocol': 'https' if request.is_secure() else 'http'
            })
            assigned_to = Task.objects.get(pk=tasksID).assigned_to.email
            email = EmailMessage(mail_subject, message, to=[assigned_to])
            email.send()

        tasksAPI = Task.objects.filter(categories=request.data['categories'])
        categoryName = Categories.objects.get(pk=request.data['categories']).name
        return Response({'data': TasksSerializers(tasksAPI, many=True).data,
                         'category': categoryName})
    return HttpResponseNotFound("Wrong request method. Try again.")


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def archiveTask(request):
    if request.method == 'PUT':
        taskID = request.data['id']
        del request.data['id']
        tasksAPI = Task.objects.filter(categories=Task.objects.get(pk=taskID).categories.id)
        categoryName = Task.objects.get(pk=taskID).categories.name
        if request.user.id == Task.objects.get(pk=taskID).created_by.user.id:
            Task.objects.filter(pk=taskID).update(categories=1)
        return Response({'data': TasksSerializers(tasksAPI, many=True).data,
                         'category': categoryName})
    return HttpResponseNotFound("Wrong request method. Try again.")


# Delete
@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def deleteTask(request, value):
    if request.method == 'DELETE':
        categories = Task.objects.get(pk=value).categories
        if request.user.id == Task.objects.get(pk=value).created_by.user.id:
            Task.objects.get(pk=value).delete()
        tasksAPI = Task.objects.filter(categories=categories.id)
        categoryName = Categories.objects.get(pk=categories.id).name
        return Response({'data': TasksSerializers(tasksAPI, many=True).data,
                         'category': categoryName})
    return HttpResponseNotFound("Wrong request method. Try again.")

# ToDos

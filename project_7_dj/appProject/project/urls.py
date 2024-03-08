from django.urls import path
from . import views

urlpatterns = [
    path('signup', views.signup),
    path('signin', views.signin),
    path('logout', views.userLogout),
    path('profile', views.profile),
    path('developers', views.getDevelopers),
    # tasks get
    path('gettasks/<int:value>/', views.getTasks),
    path('getcategories', views.getCategories),
    path('getarchive/<int:value>/', views.getArchive),
    # tasks post
    path('addtask', views.addTask),
    path('sendinvite', views.sendInvite),
    path('passwordrecovery', views.recoveryPassword),
    path('passwordchange', views.passwordChange),
    # tasks put
    path('updatetitle', views.updateTask),
    path('updatedescription', views.updateDescription),
    path('updatedraggable', views.updateDraggable),
    path('updateassigned', views.updateAssigned),
    # task archive put
    path('archivetask', views.archiveTask),
    # task delete
    path('deletetask/<int:value>', views.deleteTask)
]

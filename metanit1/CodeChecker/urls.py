from django.urls import path, include

# import views

from . import views

urlpatterns = [
    path('', views.base, name="basepage"),
    path('compiler/', views.compiler, name='compiler'),
    path('iscorrect', views.iscorrect, name="iscorrect"),
    path('signup/', views.signup, name='signup'),
    path('signin/', views.signin, name='signin'),
    path('profile/', views.profile, name='profile'),
    path('progress/', views.progress, name='progress'),
    path('logout/', views.user_logout, name='logout'),
    path('runcode', views.runcode, name="runcode"),
    path('about/', views.about, name="about"),
    path('faq_list', views.faq_list, name='faq_list'),
    path('add_faq', views.add_faq, name='add_faq'),
    path('faq/<int:faq_id>/', views.view_faq, name='view_faq'),
    path('tasks/', views.task_list, name='task_list'),
    path('tasks/<int:task_id>/', views.task_detail, name='task_detail'),
    path('tasks/<int:task_id>/run_task_code', views.run_task_code, name='run_task_code'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
    path('lectures/', views.lecture_list, name='lecture_list'),
    path('lectures/<int:lecture_id>/', views.lecture_detail, name='lecture_detail'),
]
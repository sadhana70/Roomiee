from django.urls import path, include
from . import views

app_name = 'hostel'
urlpatterns = [
    path('', views.indexx, name='indexx'),
    path('index/register/', views.register, name='register'),
    path('index/', views.index, name='index'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.logout1, name='logout'),
    path('indexx/', views.indexx, name='indexx'),

    path('signin', views.signin, name='signin'),
    path('signup/', views.signup, name='signup'),
    path('allocate/', views.allocate, name='allocate'),
    path('/stud_details/', views.student_details, name='student_details'),
    path('/change/', views.change, name='change'),
    path('change_req/', views.change_request, name='change_req'),
    path('/swap/', views.swap, name='swap'),
    path('/swap_req/', views.swap_request, name='swap_request'),
    path('/success/', views.success, name='success'),
    path('/swap_ack/', views.swap_ack, name='swap_ack'),
    path('/deallocate/', views.deallocate, name='deallocate'),
    path('/show_request/', views.show_request, name='show_request'),
    path('/show_vacancy/', views.vacant_room, name='show_vacancy'),
    path('/show_students/', views.show_students, name='show_students'),
]
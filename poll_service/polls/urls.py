from django.urls import path

from polls import views

app_name = 'polls'

urlpatterns = [
    path('', views.index, name='index'),
    path(
        'polls/<int:question_id>/',
        views.question_detail,
        name='question_detail'
    ),
    path(
        'polls/<int:question_id>/results/',
        views.results,
        name='results'
    ),
    path(
        'polls/<int:question_id>/vote/',
        views.vote,
        name='vote'
    ),
    path(
        'polls/users/',
        views.all_users,
        name='all_users'
    ),
    path('profile/<str:username>/', views.profile, name='profile'),
]

from django.urls import path

from . import views

app_name = 'myHGapp'
urlpatterns = [
    # ex: /myhgapp/
    path('', views.index, name='index'),
    # ex: /myhgapp/5/
    path('<int:question_id>/', views.detail, name='detail'),
    # ex: /pools/5/results/
    path('<int:question_id>/results/', views.results, name='results'),
    # ex: /pools/5/vote/
    path('<int:question_id>/vote', views.vote, name='vote'),
]

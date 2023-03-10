from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('doppler/', views.doppler, name = 'doppler'),

    #  path('agentlogin',views.agentlogin, name="agentlogin"),
    # path('insurance',views.insurance, name="insurance"),
    # path('<str:username>/',views.profile, name="profile"),
]
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('doppler/', views.doppler, name = 'doppler'),
    path('infrared/', views.infrared, name = 'infrared'),
    path('infrared/calibration/', views.calibrationconstant, name = 'calibration constant'),
    path('infrared/refractiveindex/', views.refractiveindex, name = 'refractive index'),
    path('infrared/wavelength/', views.wavelength, name = 'wavelength'),

    #  path('agentlogin',views.agentlogin, name="agentlogin"),
    # path('insurance',views.insurance, name="insurance"),
    # path('<str:username>/',views.profile, name="profile"),
]
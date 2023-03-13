from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

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
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
from django.urls import path
from . views import *
from rest_framework import routers
from rest_framework_simplejwt import views as jwt_views
# from . import views as aboutview
from django.conf.urls import include 


router = routers.DefaultRouter()
router.register('natalfirsttime', NatalFirstTimeViewSet),
router.register('userregistration', UserRegistrationViewSet)
router.register('usersetting', UserSettingViewSet)




urlpatterns = [
    

    path('', include(router.urls)),
    
    
    ]

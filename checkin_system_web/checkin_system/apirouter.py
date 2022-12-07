# from rest_framework.routers import DefaultRouter
from checkin_system.api import apiviews
from django.urls import path
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'Hrdata', apiviews.HrdataViewSet)
router.register(r'Checkindata', apiviews.CheckindataViewSet)

urlpatterns = router.urls
urlpatterns += [
    path('checkin/', apiviews.ChekinView.as_view(), name='checkin'),
    path('SupervisorCheck/',
         apiviews.SupervisorCheckView.as_view(),
         name='SupervisorCheck'),
]

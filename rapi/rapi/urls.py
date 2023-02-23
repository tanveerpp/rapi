from rest_framework import routers
from django.contrib import admin
from django.urls import path,include
from home.models import Emp
from home.Empserializer import EmpSerializer
from home.Empviewset import EmpViewset
from home.Productviewset import ProductViewset
router = routers.DefaultRouter()
router.register(r'emps', EmpViewset)
router.register(r'product', ProductViewset)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]

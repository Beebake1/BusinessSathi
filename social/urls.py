from django.urls import path
from .views import *
app_name = 'social'
urlpatterns = [
    # path('',testPage,name="testPage"),
    path('',social_index,name="social_index"),
    path('test',testPage,name="test"),

]


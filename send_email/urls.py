from django.contrib import admin
from django.urls import path,include
from .views import ContactView,SuccessView,IndexView

urlpatterns = [
  path("",IndexView.as_view(),name="index"),
  path("contact/",ContactView.as_view(),name="contact"),
  path("success/",SuccessView.as_view(),name="success"),
]

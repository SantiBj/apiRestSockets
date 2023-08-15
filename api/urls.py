from django.urls import path
from .views import CustomerCreateAPIView,CustomerListAPIView,CustomerRetrieveAPIView

urlpatterns = [
    path("customer/",CustomerListAPIView.as_view()),
    path("customer/<int:id>",CustomerRetrieveAPIView.as_view()),
    path("create-customer/",CustomerCreateAPIView.as_view(),name="createCustomer"),
]

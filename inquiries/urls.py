from django.urls import path
from .views import InquiryListView, InquiryDetailView

urlpatterns = [
    path('inquiries/', InquiryListView.as_view()),
    path('inquiries/<int:pk>/', InquiryDetailView.as_view()),
]
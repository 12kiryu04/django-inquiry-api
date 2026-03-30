from django.urls import path
from .views import InquiryListCreateView, InquiryDetailView

urlpatterns = [
    path('inquiries/', InquiryListCreateView.as_view()),
    path('inquiries/<int:pk>/', InquiryDetailView.as_view()),
]
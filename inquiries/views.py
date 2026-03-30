#from rest_framework.views import APIView
#from rest_framework.response import Response
#from rest_framework import status
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .models import Inquiry
from .serializers import InquirySerializer


class InquiryListCreateView(generics.ListCreateAPIView):
    serializer_class = InquirySerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = Inquiry.objects.filter(user=self.request.user)

        status_param = self.request.GET.get('status')
        priority_param = self.request.GET.get('priority')

        if status_param:
            queryset = queryset.filter(status=status_param)

        if priority_param:
            queryset = queryset.filter(priority=priority_param)

        return queryset
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
    
class InquiryDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = InquirySerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Inquiry.objects.filter(user=self.request.user)
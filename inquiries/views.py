from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

from .models import Inquiry
from .serializers import InquirySerializer


class InquiryListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        inquiries = Inquiry.objects.filter(user=request.user)

        status_param = request.GET.get('status')
        priority_param = request.GET.get('priority')

        if status_param:
            inquiries = inquiries.filter(status=status_param)

        if priority_param:
            inquiries = inquiries.filter(priority=priority_param)

        serializer = InquirySerializer(inquiries, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = InquirySerializer(data=request.data)

        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class InquiryDetailView(APIView):
    permission_classes = [IsAuthenticated]

    def get_object(self, pk, user):
        try:
            return Inquiry.objects.get(pk=pk, user=user)
        except Inquiry.DoesNotExist:
            return None

    def get(self, request, pk):
        inquiry = self.get_object(pk, request.user)
        if inquiry is None:
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)

        serializer = InquirySerializer(inquiry)
        return Response(serializer.data)

    def put(self, request, pk):
        inquiry = self.get_object(pk, request.user)
        if inquiry is None:
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)

        serializer = InquirySerializer(inquiry, data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        inquiry = self.get_object(pk, request.user)
        if inquiry is None:
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)

        inquiry.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
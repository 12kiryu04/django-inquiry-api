from dataclasses import fields
from rest_framework import serializers
from .models import Inquiry

class InquirySerializer(serializers.ModelSerializer):
    class Meta:
        model = Inquiry
        fields = '__all__'
        read_only_fields = ['user', 'created_at', 'updated_at']
        
    def validate_title(self, value):
        if len(value) < 3:
            raise serializers.ValidationError("3文字以上にしてください")
        return value
from rest_framework import serializers
from .models import user_info  # Replace with your actual model name

class user_ser(serializers.ModelSerializer):
    class Meta:
        model = user_info
        fields = '__all__'  # Or list specific fields if you don't want to include all

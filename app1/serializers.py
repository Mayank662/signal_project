from rest_framework import serializers
from .models import Model1

# simple serializer class to validate Model1
class Model1Serializer(serializers.ModelSerializer):
    class Meta:
        model = Model1
        fields = '__all__'

    def validate_field1(self, value):
        if len(value) > 10:
            raise serializers.ValidationError("string length need to be less than 10")
        
    def validate_field3(self, value):
        if value > 1000:
            raise serializers.ValidationError("value need to be less than 1000")
        
    def validate_field2(self, value):
        if not value:
            raise serializers.ValidationError("value need to be less than 1000")
    
    def validate_field4(self, value):
        if not value:
            raise serializers.ValidationError("value need to be less than 1000")
